from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title=website, message=f"email: {data[website]['email']}\n"
                                                       f"password: {data[website]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Error", message="No details for the website exist")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

                website_entry.delete(0, END)
                password_entry.delete(0, END)
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
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1, sticky="w")
website_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "testemail@git.com")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=create_password)
generate_password_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="w")

window.mainloop()
