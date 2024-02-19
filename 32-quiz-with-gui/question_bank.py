import requests
import html
parameters = {
    'amount': 10,
    'difficulty': 'easy',
    'type': 'boolean'

}

response = requests.get('https://opentdb.com/api.php', params=parameters).json()
questions = response['results']
# print(questions)


class QuestionBank:
    def __init__(self):
        # self.question = question
        # self.answer = answer
        self.bank = get_data()


def get_data():
    bank = []
    for i in questions:
        question = html.unescape(i['question'])
        answer = i['correct_answer']
        bank.append({
            'question': question,
            'answer': answer
        })
    return bank
