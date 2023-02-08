from tkinter import *
MULTIPLYING = 1.609344


def convert():
    miles = float(entry.get())
    km = round(miles * MULTIPLYING, 2)
    label_converted.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=50, pady=50)

# Text, Label section
label_miles = Label(text="Miles", font=("Arial", 12))
label_miles.grid(column=2, row=0)

label_is_equal_to = Label(text="is equal to", font=("Arial", 12))
label_is_equal_to.grid(column=0, row=1)

label_km = Label(text="Km", font=("Arial", 12))
label_km.grid(column=2, row=1)

label_converted = Label(text="0", font=("Arial", 12))
label_converted.grid(column=1, row=1)

# Entry section
entry = Entry(width=10)
entry.grid(column=1, row=0)
entry.insert(END, string="0")
entry.focus()

# Button section
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)


window.mainloop()
