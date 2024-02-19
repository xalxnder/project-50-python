from question_model import QuiZQuestion
from data import question_data
from quiz_brain import *

question_bank = []
for q in question_data:
	q_text = q["question"]
	q_answer = q["correct_answer"]
	question = QuiZQuestion(q_text, q_answer)
	question_bank.append(question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
	quiz.next_question()
else:
	print(f"All done, your final score is {quiz.score}")
