import time

import pandas as pd
from revChatGPT.V1 import Chatbot

from questioner import Questioner, questions

class ChatGPTQuestioner(Questioner):
    def __init__(self, config_path, prompt) -> None:
        super().__init__(config_path, prompt)

        self.chatbot = Chatbot(config={
            'email': self.config['email'],
            'password': self.config['password'],
            'model': 'gpt-4',
        })

    def ask_question(self, question):
        answer_text = self.chatbot.ask(self.prompt + '\n' + question)
        time.sleep(self.config['delay'])
        return answer_text

if __name__ == '__main__':
    questioner = ChatGPTQuestioner('config/chat_gpt_config.yaml', 'Answer the following question: ')
    question_answer_sheet = pd.read_json('data/question-answer-sheet.json')
    answer_df = questions(questioner, question_answer_sheet, 'data/result/chat_gpt_answer.csv')
