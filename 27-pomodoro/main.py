from tkinter import *
import time
import math

REPS = 0

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=508)
# Todo - Set Up GUI
canvas = Canvas(width=200, height=224, highlightthickness=0)

# Place tomato in center of screen
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", tags="test")
canvas.grid(row=1, column=1)
timer_name = None
checkmark_label = ""

# TODO - Start Mechanism
def start():
    global REPS
    if REPS <= 8:
        print(REPS)
        REPS += 1
        if REPS == 8:
            timer_label["text"] = "Long Break :)"
            count_down(20 * 60)
        elif REPS % 2 == 0:
            timer_label["text"] = "Break"
            count_down(5 * 60)
            checkmark['text'] += "✓"
        else:
            timer_label["text"] = "Work"
            count_down(25 * 60)
    else:
        timer_label["text"] = "All Done ! 🎉"


def reset():
    """This resets the timer"""
    window.after_cancel(timer_name)
    start_button['state'] = NORMAL
    canvas.itemconfig(timer_text, text="00:00")
    timer_label["text"] = "Timer"
    checkmark['text'] = ""
    global REPS
    REPS = 0


def count_down(count):
    """Timer countdown mechanism."""
    start_button['state'] = DISABLED
    global timer_name
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02}")
    if count > 0:
        timer_name = window.after(1000, count_down, count - 1)
    else:
        start()




# Place start and reset Buttons
start_button = Button(window, text="Start", command=start)
start_button.grid(row=3, column=0)
reset_button = Button(window, text="Reset", command=reset)
reset_button.grid(row=3, column=3)

# Place the word "Timer" above tomato
timer_label = Label(text="", font=('Helvetica', 30))
timer_label.grid(row=0, column=1)

# Checkmarks
checkmark = Label(text="", font=('Helvetica', 30))
checkmark.grid(row=3, column=1)


window.mainloop()
