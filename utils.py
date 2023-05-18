import re
import pandas as pd
from questioner import Questioner

def find_answer(answer_text) -> int:
    num_lt = re.findall(r'\([1-5]\)', answer_text)
    if len(num_lt) != 0:
        num_lt = [int(num[1:-1]) for num in num_lt]
        answer = num_lt[-1]
    else:
        numbers = re.findall(r'\d+', answer_text)
        answer = int(numbers[-1])

    return answer

def questions(questioner: Questioner, question_answer_sheet: pd.DataFrame, result_path):
    answer_df = questioner.ask_multiple_question(question_answer_sheet)
    answer_df.to_csv(result_path, index=False)

    return answer_df
