import pandas as pd
from revChatGPT.V1 import Chatbot

from questioner import Questioner, questions
from utils import replace_to_parenthesis

class ChatGPTQuestioner(Questioner):
    def __init__(self, config_path, prompt) -> None:
        super().__init__(config_path, prompt)

        self.chatbot = Chatbot(config={
            'email': self.config['email'],
            'password': self.config['password'],
            'model': 'gpt-4',
        })

    def question(self, question):
        answer_text = self.chatbot.ask(self.prompt + '\n' + question)
        return answer_text

if __name__ == '__main__':
    questioner = ChatGPTQuestioner('config/chat_gpt_config.yaml', 
                                   prompt='다음 문제를 풀어줘. 선택지가 있으면 선택지를 골라줘.'
    )
    question_answer_sheet = pd.read_csv('data/KoreanSAT.csv')
    question_answer_sheet = question_answer_sheet.apply(replace_to_parenthesis, axis=0)
    answer_df = questions(questioner, question_answer_sheet, 'data/result/chat_gpt_answer.csv')
