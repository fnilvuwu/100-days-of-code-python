from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    user_website = website_input.get()
    user_password = password_input.get()
    user_username = username_input.get()
    new_data = {
        user_website: {
            "email": user_username,
            "password": user_password,
        }
    }
    if len(user_password) < 1 or len(user_username) < 1 or len(user_website) < 1:
        messagebox.showwarning(title="Oops", message="Don't leave any field empty!")
    else:
        try:
            file = open("data.json", "r")
            #read old data
            data = json.load(file)
            #update old data with new data
            data.update(new_data)

            file = open("data.json", "w")
            #save updated data
            json.dump(data, file, indent=4)
            website_input.delete(0, END)
            password_input.delete(0, END)
            file.close()
        except FileNotFoundError:
            file = open("data.json", "w")
            #save updated data
            json.dump(new_data, file, indent=4)
            website_input.delete(0, END)
            password_input.delete(0, END)
            file.close()

def find_password():
    user_website = website_input.get()
    try:
        file = open("data.json", "r")
        #read old data
        data = json.load(file)
        #update old data with new data
        if user_website in data:
            for (key, value) in data.items():
                if user_website == key:
                    messagebox.showinfo(title=key, message=f'Email: {value["email"]}\nPassword: {value["password"]}')
        else:
            messagebox.showwarning(title="Not Found", message="No details for the website exists")
        file.close()
    except FileNotFoundError:
        messagebox.showerror(title="No Data File Found", message="Please Add Data")
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
myImg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=myImg)
canvas.grid(column=0, row=0, columnspan=3)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.config(padx=5, pady=5)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_label.config(padx=5, pady=5)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_label.config(padx=5, pady=5)
#Buttons
search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate", width=12, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

#Entry/Input
website_input = Entry(width=19)
website_input.grid(column=1, row=1, pady=5)
website_input.focus()

username_input = Entry(width=38)
username_input.grid(column=1, row=2, columnspan=2, padx=10 ,pady=5)
username_input.insert(0, "example@email.com")

password_input = Entry(width=19)
password_input.grid(column=1, row=3, pady=5)

window.mainloop()