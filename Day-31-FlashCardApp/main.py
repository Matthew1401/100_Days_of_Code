from tkinter import *
import pandas
import random
FONT_UP = ("Ariel", 40, "italic")
FONT_DOWN = ("Ariel", 60, "bold")

# Data reading
data = pandas.read_csv("ang_pl.csv")
english_words = data.English.to_list()
polish_words = data.Polish.to_list()
list_length = len(english_words)


def pick_word():
    index = random.randint(0, list_length - 1)
    canvas.itemconfig(eng_word, text=english_words[index])


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg='#B1DCC5')


canvas = Canvas(width=800, height=526, bg='#B1DCC5', highlightthickness=0)
card_front_png = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_png)
canvas.create_text(400, 150, text="English", font=FONT_UP)
eng_word = canvas.create_text(400, 263, text="up", font=FONT_DOWN)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg='#B1DCC5', command=pick_word)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg='#B1DCC5', command=pick_word)
wrong_button.grid(column=0, row=1)


window.mainloop()
