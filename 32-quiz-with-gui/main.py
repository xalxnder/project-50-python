import requests
import random
from random import randint
from ui import *
from question_bank import *
from quiz import *
question_bank = QuestionBank().bank
quiz = Quiz(question_bank)
quiz_ui = QuizUI(quiz)



