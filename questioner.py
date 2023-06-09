from tqdm import tqdm
import yaml
import time
import pandas as pd
import numpy as np
from utils import find_answer

class Questioner:
    def __init__(self, config_path, prompt) -> None:
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        self.prompt = prompt

    def question(self, question):
        raise NotImplementedError
    
    def ask_question(self, question):
        answer = self.question(question)
        time.sleep(
            np.clip(np.random.normal(loc=self.config['delay'], scale=5), 
                    self.config['delay'] - 5,
                    self.config['delay'] + 5
                    )
        )
        return answer
    
    def mark(self, question, correct):
        answer_text = self.ask_question(question)
        answer = find_answer(question, answer_text)

        return answer, (answer == correct)
    
    def ask_multiple_question(self, question_df):
        answer_dict = {}
        answer_dict['Answer'] = []
        answer_dict['Correct'] = []

        for _, question in tqdm(question_df.iterrows()):
            question_text = question['Question']
            correct_answer = question['CorrectAnswer']
            answer, correct = self.mark(question_text, correct_answer)
            answer_dict['Answer'].append(answer)
            answer_dict['Correct'].append(correct)
        
        return pd.DataFrame(answer_dict)

def questions(questioner: Questioner, question_answer_sheet: pd.DataFrame, result_path):
    answer_df = questioner.ask_multiple_question(question_answer_sheet)
    answer_df.to_csv(result_path, index=False)

    return answer_df
