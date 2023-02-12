from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    data_text = website_entry.get() + " | " + email_entry.get() + " | " + password_entry.get() + "\n"
    # with open("data.txt", mode="a") as file:
    #     file.write(data_text)
    print(data_text)
    website_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Logo
canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=("Courier", 10))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=("Courier", 10))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Courier", 10))
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "testemail@git.com")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()
