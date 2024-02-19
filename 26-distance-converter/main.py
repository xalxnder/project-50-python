from tkinter import *

window = Tk()
window.title("Distance Converter")

placeholder_text = Label(text="Kilometers is equal to")
placeholder_text.grid(row=1, column=2)

answer_text = Label(text="0")
answer_text.grid(row=1, column=5)

unit_text = Label(text="Miles")
unit_text.grid(row=1, column=6)

user_input = Entry(width=10)
user_input.grid(row=1, column=0)


def show_answer():
    miles = int(user_input.get()) * .62
    answer_text.config(text=miles)


calculate = Button(window, text="Calculate", command=show_answer)
calculate.grid(row=4, column=2)

window.mainloop()
