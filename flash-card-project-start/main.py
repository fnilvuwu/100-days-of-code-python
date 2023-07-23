from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
BLACK = "#000000"
WHITE = "#FFFFFF"

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

data_in_list_dict = data.to_dict(orient="records")
current_card = {}

def known_word():
    try:
        data_in_list_dict.remove(current_card)
        new_data = pandas.DataFrame(data_in_list_dict)
        new_data.to_csv("words_to_learn.csv")
        random_french()
    except:
        messagebox.showwarning(title="Oops", message="Words not exist in words to learn!")

def random_french():
    try:
        global current_card, timer
        window.after_cancel(timer)
        current_card = random.choice(data_in_list_dict)
        french_word = current_card["French"]
        canvas.itemconfig(language_name, text="French", fill=BLACK)
        canvas.itemconfig(french_text, text=french_word, fill=BLACK)
        canvas.itemconfig(card_canvas, image=card_front)
        timer = window.after(3000, show_english)
    except:
        messagebox.showwarning(title="Oops", message="No more data remain in words to learn")
    
def show_english():
    english_word = current_card["English"]
    canvas.itemconfig(language_name, text="English", fill=WHITE)
    canvas.itemconfig(french_text, text=english_word, fill=WHITE)
    canvas.itemconfig(card_canvas, image=card_back)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, show_english)

correct_image = PhotoImage(file="images/right1.png")
wrong_image = PhotoImage(file="images/wrong1.png")

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas = canvas.create_image(400, 263)
canvas.grid(column=0, row=1, columnspan=2)
language_name = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
french_text = canvas.create_text(400, 263, font=("Arial", 60, "bold"))

correct_button = Button(image=correct_image, highlightthickness=0, activebackground=BACKGROUND_COLOR, command=known_word)
correct_button.config(bg=BACKGROUND_COLOR, bd=0)
correct_button.grid(column=0, row=2)


wrong_button = Button(image=wrong_image, highlightthickness=0, activebackground=BACKGROUND_COLOR, command=random_french)
wrong_button.config(bg=BACKGROUND_COLOR, bd=0)
wrong_button.grid(column=1, row=2)
    
try:
    random_french()
except:
    data = pandas.read_csv("data/french_words.csv")
    data.to_csv("words_to_learn.csv")
    data_in_list_dict = data.to_dict(orient="records")
    random_french()

window.mainloop()