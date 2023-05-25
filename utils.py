import re

def find_answer(question, answer_text, is_multiple_choice=True) -> int:
    if is_multiple_choice:
        num_lt = re.findall(r'\([1-5]\)', answer_text)

        if len(num_lt) != 0:
            num_lt = [int(num[1:-1]) for num in num_lt]
            choice = num_lt[-1]
        else:
            choice_line_lt = (question[question.find('('):]
                       .strip()
                       .split('\n')
                       .strip()
                       )
            choice_dict = {} # answer: choice_number (값: 선지 번호)
            for choice_line in choice_line_lt:
                choice = re.findall(r'\([1-5]\)', choice_line)[0]
                answer = int(choice_line[choice_line.find(')') + 1:].strip())
                choice_dict[answer] = choice

            numbers = re.findall(r'\d+', answer_text)
            answer = int(numbers[-1])
            choice = choice_dict[answer]
    else:
        numbers = re.findall(r'\d+', answer_text)
        answer = int(numbers[-1])
        choice = answer
    
    return choice
