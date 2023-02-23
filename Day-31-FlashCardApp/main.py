from tkinter import *
import pandas
import random
FONT_UP = ("Ariel", 40, "italic")
FONT_DOWN = ("Ariel", 60, "bold")
index = None
timer = None
is_card_front = False


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
def pick_word():
    global index, is_card_front
    index = random.randint(0, words_length - 1)
    if is_card_front:
        canvas.itemconfig(displaying_word, text=words[index]['English'])
    else:
        canvas.itemconfig(displaying_word, text=words[index]['Polish'])


def card_front():
    global index
    canvas.itemconfig(displaying_word, text=words[index]['English'], fill='black')
    canvas.itemconfig(title_word, text='English', fill='black')
    canvas.itemconfig(card, image=card_front_png)


def card_back():
    global index
    canvas.itemconfig(displaying_word, text=words[index]['Polish'], fill='white')
    canvas.itemconfig(title_word, text='Polski', fill='white')
    canvas.itemconfig(card, image=card_back_png)


def application_on():
    global index, timer, is_card_front
    if is_card_front:
        card_back()
        is_card_front = False
    else:
        card_front()
        is_card_front = True
    timer = window.after(3000, application_on)


def save_word():
    global index
    words.remove(words[index])
    save = {
        'English': [i['English'] for i in words],
        'Polish': [i['Polish'] for i in words]
    }
    df = pandas.DataFrame(save)
    df.to_csv("words_to_learn.csv", index=False)


# -----------------------------------------------------UI------------------------------------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg='#B1DCC5')


canvas = Canvas(width=800, height=526, bg='#B1DCC5', highlightthickness=0)
card_front_png = PhotoImage(file="images/card_front.png")
card_back_png = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_png)
title_word = canvas.create_text(400, 150, text="English", font=FONT_UP)
displaying_word = canvas.create_text(400, 263, text="", font=FONT_DOWN)
pick_word()
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg='#B1DCC5', command=save_word)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg='#B1DCC5', command=pick_word)
wrong_button.grid(column=0, row=1)


application_on()
window.mainloop()
