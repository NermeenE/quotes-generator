from tkinter import *
import random
import requests

def get_quote():
    response = requests.get(url="https://type.fit/api/quotes")
    response.raise_for_status()

    data = response.json()
    quote_dict = random.choice(data)["text"]
    canvas.itemconfig(quote_text, text=quote_dict)
    
window = Tk()
window.title("Inspirational Quotes")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="img/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="INSPIRALTION\nQUOTES", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

brain_img = PhotoImage(file="img/brain.png")
brain_button = Button(image=brain_img, highlightthickness=0, command=get_quote)
brain_button.grid(row=1, column=0)


window.mainloop()