from tkinter import *
import pandas as pd
import random
import time
from tkinter import messagebox


class QuizUI:
    def __init__(self, quiz):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quiz App')
        self.score_text = Label(text='Score: 0', fg='black', bg='#B1DDC6')
        self.score_text.grid(column=1, row=0)
        self.window.config(padx=20, pady=20, background='#B1DDC6')
        self.canvas = Canvas(width=380, height=350, background="white", highlightthickness=0)
        self.quote = self.canvas.create_text(190, 175, text="Question Text", font=("Helvetica", 20), fill="black",
                                             width=250)
        self.canvas.grid(padx=20, pady=50, column=0, row=1, columnspan=2)
        self.true_check = PhotoImage(file="images/true.png")
        self.false_x = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_check, highlightthickness=0, text='True', command=self.check_true)
        self.false_button = Button(image=self.false_x, highlightthickness=0, text='True', command=self.check_false)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
        self.display_next_question()
        self.window.mainloop()

    def display_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.questions_left():
            self.score_text.config(text=f'Score: {self.quiz.score}')
            # print(f'Your score is {self.quiz.score}')
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote, text=question_text)
        else:
            self.canvas.itemconfig(self.quote, text='Game Over')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def check_true(self):
        self.player_feedback(self.quiz.check_answer('True'))

    def check_false(self):
        self.player_feedback(self.quiz.check_answer('False'))

    def player_feedback(self, correct) :
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.display_next_question)
