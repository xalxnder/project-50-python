import requests
import random
from random import randint
from ui import *


class Quiz:
    def __init__(self, question_list):
        self.score = 0
        self.question_number_index = 0
        self.question_list = question_list
        self.current_question = None

    def questions_left(self):
        return self.question_number_index <= (len(self.question_list) - 1)

    def next_question(self):
        self.current_question = self.question_list[self.question_number_index]
        user_input = f"{self.current_question['question']}"
        self.question_number_index += 1
        return user_input

    def check_answer(self, button) -> bool:
        if button == self.current_question['answer']:
            self.score += 1
            return True
        else:
            return False
