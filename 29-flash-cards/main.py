from tkinter import *
import pandas as pd
import random
import time
from tkinter import messagebox

DATA_LOCATION = "data/french_words.csv"
WORDS = pd.read_csv(DATA_LOCATION, delimiter=",")
list_of_words = WORDS.to_dict(orient="records")

# Set Up UI
window = Tk()
window.title("Flash Cards")
window.config(background="#B1DDC6")


def random_word():
    shuffled_word = list_of_words[random.randint(0, len(list_of_words))]['French']
    canvas.itemconfig(canvas_card, image=front)
    title.config(text="French", background="white")
    word.config(text=shuffled_word, background="white")
    window.after(3000, flip)


def check_correct_answer():
    for i in range(len(list_of_words) - 1):
        if list_of_words[i]["English"] == word["text"]:
            print(word["text"])
            print(list_of_words[i]["English"])
            del list_of_words[i]
            return True


def correct_answer():
    if check_correct_answer():
        random_word()


initial_shuffled_word = list_of_words[random.randint(0, len(list_of_words))]['French']


def flip():
    for i in range(len(list_of_words) - 1):
        if list_of_words[i]["French"] == word["text"]:
            word.config(text=list_of_words[i]["English"], background="#91C2AF")
    canvas.itemconfig(canvas_card, image=back)
    title.config(text="English", background="#91C2AF")


# Images
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=700, background="#B1DDC6", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
canvas_card = canvas.create_image(408, 400, image=front)

# Labels
title = Label(text="French", foreground="black", background="white")
title.config(font=("Arial", 40))
word = Label(text=initial_shuffled_word, foreground="black", background="white")
word.config(font=("Arial", 60, "bold"))

# Buttons
correct_button = Button(image=correct_image, highlightthickness=0, command=correct_answer)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_word)

# Positions
correct_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)
word.place(x=322, y=380)
title.place(x=330, y=200)

window.after(3000, flip)

window.mainloop()
