from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
is_timer_on = False
is_counting_on = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global is_counting_on
    global is_timer_on
    is_counting_on = False
    is_timer_on = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def global_timer():
    global is_counting_on
    global is_timer_on
    check_mark = ""
    is_counting_on = True
    while is_counting_on:
        for _ in range(4):
            text_timer.config(text="Work")
            time_counter(WORK_MIN)
            check_mark = check_mark + "✔"
            checking_label.config(text=check_mark)
            if not is_counting_on:
                break
            text_timer.config(text="Break")
            time_counter(SHORT_BREAK_MIN)
            if not is_counting_on:
                break
        if not is_counting_on:
            break
        checking_label.config(text="")
        check_mark = ""
        time_counter(LONG_BREAK_MIN)

    text_timer.config(text="Timer")
    checking_label.config(text="")
    canvas.itemconfig(text_id, text="00:00")


def time_counter(minutes):
    global is_counting_on
    global is_timer_on
    canvas.itemconfig(text_id, text=f"{minutes}:00")
    seconds = 0
    is_timer_on = True
    while is_timer_on:
        window.update()
        time.sleep(0.1)
        if seconds == 0:
            minutes -= 1
            seconds = 60
            if minutes == 0:
                minutes = "00"

        seconds -= 1
        countdown(minutes, seconds)

        if minutes == "00" and seconds == 0:
            is_timer_on = False


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(minutes, seconds):
    if seconds == 60:
        canvas.itemconfig(text_id, text=f"{minutes}:00")
    elif seconds > 9:
        canvas.itemconfig(text_id, text=f"{minutes}:{seconds}")
    else:
        canvas.itemconfig(text_id, text=f"{minutes}:0{seconds}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
text_id = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

text_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
text_timer.grid(column=1, row=0)

button_start = Button(text="Start", command=global_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset)
button_reset.grid(column=2, row=2)

checking_label = Label(text="", fg=GREEN, bg=YELLOW)
checking_label.grid(column=1, row=3)


window.mainloop()
