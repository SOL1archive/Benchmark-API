import pandas as pd
import requests
from bardapi import Bard

from questioner import Questioner, questions

class BardQuestioner(Questioner):
    def __init__(self, config_path, prompt) -> None:
        super().__init__(config_path, prompt)

        api_key = self.config['api_key']
        self.prompt = prompt

        self.session = requests.Session()
        self.session.headers = {
                    "Host": "bard.google.com",
                    "X-Same-Domain": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "Origin": "https://bard.google.com",
                    "Referer": "https://bard.google.com/",
                }
        self.session.cookies.set("__Secure-1PSID", api_key)

        self.bard = Bard(token=api_key, session=self.session)
        
    def ask_question(self, question):
        answer = self.bard.get_answer(self.prompt + '\n' + question)['content']
        return answer

if __name__ == '__main__':
    questioner = BardQuestioner('config/bard_config.yaml', 'Answer the following question. If the problem is multiple: ')
    question_answer_sheet = pd.read_json('data/question-answer-sheet.json')
    answer_df = questions(questioner, question_answer_sheet, 'data/result/bard_answer.csv')
