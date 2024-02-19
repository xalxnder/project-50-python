from tkinter import *
from tkinter import messagebox
import pyperclip
import json
from password_generator import password_generator

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, background="white")
canvas = Canvas(width=256, height=256, background="white", highlightthickness=0, )
lock_image = PhotoImage(file="lock-256.png")
canvas.create_image(128, 128, image=lock_image)
canvas.grid(row=0, column=1, pady=20)


def password():
    password_text = password_input.get()
    pyperclip.copy(password_text)
    password_input.delete(0, END)
    password_input.insert(INSERT, password_generator())


def add():
    website_text = website_input.get()
    email_text = username_input.get()
    password_text = password_input.get()
    website_input.delete(0, END)
    username_input.delete(0, END)
    password_input.delete(0, END)
    json_dict = {website_text: {
        "Email": email_text,
        "Password": password_text
    }}
    if website_text == "" or email_text == "" or password_text == "":
        messagebox.showwarning("Error", "Please don't leave any fields blank")
    else:
        msg_box = messagebox.askquestion("Form", f"Email: {email_text} \nPassword: {password_text} \nReady to save?")
        if msg_box == 'yes':
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(json_dict, file, indent=4)
            else:
                data.update(json_dict)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)


def search():
    """Function that searches our data.json file"""
    # Get user input from website input
    website_text = website_input.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            matched_email = data[website_text]["Email"]
            matched_password = data[website_text]["Password"]
    except FileNotFoundError:
        print("No file found. Please enter data")
    else:
        if website_text in data:
            messagebox.showinfo("Error", f"Email:{matched_email} \nPassword:{matched_password}")


# Entry Boxes
password_input = Entry(width=21, background="white", foreground="black")
website_input = Entry(width=21, background="white", foreground="black", highlightthickness=0)
username_input = Entry(width=35, background="white", foreground="black", highlightthickness=0)

# Labels
password_input_label = Label(text="Password:", foreground="black", background="white")
website_input_label = Label(text="Website", foreground="black", background="white")
username_input_label = Label(text="Username/Email:", foreground="black", background="white")

# Buttons
generate_password = Button(text="Generate Password", highlightbackground="white", command=password)
add_button = Button(text="Add", width=36, highlightbackground="white", command=add)
search_button = Button(text="Search", highlightbackground="white", command=search)

# Positions
website_input_label.grid(row=1, column=0)
password_input_label.grid(row=3, column=0)
password_input.grid(column=1, row=3, sticky="EW")
website_input.grid(row=1, column=1, sticky="EW")
add_button.grid(row=4, column=1, columnspan=2)
search_button.grid(row=1, column=2, sticky="EW")
generate_password.grid(column=2, row=3, sticky="EW")
username_input_label.grid(row=2, column=0)
username_input.grid(row=2, column=1, columnspan=2, sticky="EW")

window.mainloop()
