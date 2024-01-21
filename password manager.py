from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def search():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found.")
    else:
        if website in data:
            username = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email/Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details available for {website}.")


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
# x, y, position
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_lbl = Label(text="Website:")
website_lbl.grid(row=1, column=0)
username_lbl = Label(text="Email/Username:")
username_lbl.grid(row=2, column=0)
pass_lbl = Label(text="Password:")
pass_lbl.grid(row=3, column=0)

website_entry = Entry(width=27)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = Entry(width=45)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "sahil@gmail.com")
pass_entry = Entry(width=27)
pass_entry.grid(row=3, column=1)

generate_pass_btn = Button(text="Generate Password", command=generate_pass)
generate_pass_btn.grid(row=3, column=2)
search_btn = Button(text="Search", command=search)
search_btn.grid(row=1, column=2)
add_btn = Button(text="Add", width=38, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
