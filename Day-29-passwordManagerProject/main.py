from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

# Logo
canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

# Texts
text_website = Label(text="Website:", font=("Courier", 10))
text_website.grid(column=0, row=1)

text_email = Label(text="Email/Username:", font=("Courier", 10))
text_email.grid(column=0, row=2)

text_password = Label(text="Password:", font=("Courier", 10))
text_password.grid(column=0, row=3)

# Inputs
input_website = Entry(width=51)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_email = Entry(width=51)
input_email.grid(column=1, row=2, columnspan=2)

input_password = Entry(width=33)
input_password.grid(column=1, row=3)

# Buttons
button_gen_pass = Button(text="Generate Password")
button_gen_pass.grid(column=2, row=3, sticky="w")

button_add = Button(text="Add", width=43)
button_add.grid(column=1, row=4, columnspan=2)




window.mainloop()
