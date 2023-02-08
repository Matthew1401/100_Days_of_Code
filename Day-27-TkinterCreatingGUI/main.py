from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()


# Button
def button_clicked():
    my_label.config(text="I got clicked")


button = Button(text="Click Me", command=button_clicked)
button.pack()






window.mainloop()
