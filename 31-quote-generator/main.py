from tkinter import *
from PIL import Image, ImageTk
import requests

# Set Up UI
window = Tk()
window.title("Inspiration")
window.config(background="#B1DDC6")


def quote_generator():
    """Generate a random quote from the api-ninja api."""
    CATEGORY = 'inspirational'
    api_url = f'https://api.api-ninjas.com/v1/quotes?category={CATEGORY}'
    response = requests.get(api_url, headers={'X-Api-Key': 'API-KEY'})  # API-KEY - https://api-ninjas.com/
    data = response.json()
    quote_text = data[0]['quote']
    author = data[0]['author']
    generated_quote = f'{quote_text} \n-{author}'
    canvas.itemconfig(quote, text=generated_quote, font=("Helvetica", 15, "bold"))


# Images
quote_box_image = Image.open('images/quote_box.png')
resized_quote_box_image = quote_box_image.resize((500, 500))
final_quote_box_image = ImageTk.PhotoImage(resized_quote_box_image)

# Canvas
canvas = Canvas(width=800, height=700, background="#B1DDC6", highlightthickness=0)
canvas.grid(row=0, column=0)
canvas_card = canvas.create_image(400, 400, image=final_quote_box_image)
quote = canvas.create_text(408, 360, text="🧘🏾", width=250, font=("Helvetica", 55, "bold"), fill="black")

# Buttons
click_button = Button(text="Click Here For Inspiration", highlightthickness=0, highlightbackground="#B1DDC6",
                      command=quote_generator)
click_button.place(x=300, y=550)
window.mainloop()
