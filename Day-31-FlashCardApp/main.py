from tkinter import *
import pandas
import random
FONT_UP = ("Ariel", 40, "italic")
FONT_DOWN = ("Ariel", 60, "bold")
current_card = {}


# -------------------------------------------------Data reading------------------------------------------------------- #
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("ang_pl.csv")
finally:
    words = data.to_dict(orient="records")
    print(words)
    words_length = len(words)


# --------------------------------------------------Functions--------------------------------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(title_word, text="English", fill="black")
    canvas.itemconfig(displaying_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card, image=card_front_png)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_word, text="Polski", fill="white")
    canvas.itemconfig(displaying_word, text=current_card["Polish"], fill="white")
    canvas.itemconfig(card, image=card_back_png)


def save_word():
    words.remove(current_card)
    data = pandas.DataFrame(words)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


# -----------------------------------------------------UI------------------------------------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg='#B1DCC5')

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg='#B1DCC5', highlightthickness=0)
card_front_png = PhotoImage(file="images/card_front.png")
card_back_png = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_png)
title_word = canvas.create_text(400, 150, text="English", font=FONT_UP)
displaying_word = canvas.create_text(400, 263, text="", font=FONT_DOWN)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg='#B1DCC5', command=save_word)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg='#B1DCC5', command=next_card)
wrong_button.grid(column=0, row=1)


next_card()
window.mainloop()
