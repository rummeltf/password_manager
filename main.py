from ctypes import alignment
import tkinter as tk
from tkinter import messagebox
from tkinter import dialog
from turtle import left
import random as rand
import pyperclip as pc



# password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',\
     'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():

    letter_count = rand.randint(8, 10)
    num_count = rand.randint(2, 4)
    symbol_count = rand.randint(2, 4)

    password_letters =  [rand.choice(letters) for _ in range(letter_count)]
    password_numbers = [rand.choice(numbers) for _ in range(num_count)]
    password_symbols = [rand.choice(symbols) for _ in range(symbol_count)]
    password = password_letters + password_numbers + password_symbols

    # randomize order of characters and copy password to clipboard
    rand.shuffle(password)
    final_pw = "".join(password)
    password_input.insert(0, final_pw)
    pc.copy(final_pw)

# saving the password to the document with some info verification
def add_password():
    website = website_input.get()
    email_username = email_username_input.get() 
    password = password_input.get()

    if len(website) or len(email_username) or len(password) == 0:
        messagebox.showinfo(title="Field Empty", message="Please don't leave a field empty.")        
    else:
        verify_info = messagebox.askokcancel(title="MyPass", message=f"Information for {website}: \nEmail: {email_username} \nPassword: {password} \nPress ok to save.")
        if verify_info:
            with open(r"100_days\day_29\passwords.txt", "a") as pw_file:
                pw_file.write(f"{website}\n{email_username}\n{password}\n\n")
                website_input.delete(0, "end")
                # email_username_input.delete(0, "end") 
                # if you want to have unique emails or usernames, uncomment out the above line and comment out line 75
                password_input.delete(0, "end")

# GUI setup

window = tk.Tk()
window.title("MyPass Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
logo_image = tk.PhotoImage(file=r"100_days\day_29\logo.png") # change to your file's location
canvas.create_image(125, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:", font=("Arial", 10))
website_label.grid(column=0, row=1)

website_input = tk.Entry(width=53)
website_input.get()
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_username_label = tk.Label(text="Email/Username:", font=("Arial", 10))
email_username_label.grid(column=0, row=2)

email_username_input = tk.Entry(width=53)
email_username_input.get()  
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "put@emailaddress.here") # line to comment out if you want to customize the email/username each time

password_label = tk.Label(text="Password:", font=("Arial", 10))
password_label.grid(column=0, row=3)

password_input = tk.Entry(width=32)
password_input.get()
password_input.grid(column=1, row=3)

generate_password_button = tk.Button(text="Generate Password", font=("Arial", 10), command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", font=("Arial", 10), width=40, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()