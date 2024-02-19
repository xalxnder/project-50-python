class QuizBrain:
	def __init__(self, question_list):
		self.question_number = 0
		self.question_list = question_list
		self.score = 0

	def next_question(self):
		current_question = self.question_list[self.question_number]
		self.question_number += 1
		user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
		self.check_answer(user_answer, current_question.answer)
		return user_answer

	def still_has_questions(self):
		if self.question_number < len(self.question_list):
			return True

	def check_answer(self, user_answer, actual_answer):
		if user_answer == actual_answer:
			self.score += 1
			print("Correct")
		else:
			print(f"Wrong. The correct answer was {actual_answer}")
		print(f"Your current score is {self.score} / {len(self.question_list)}")
