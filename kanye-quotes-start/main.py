from tkinter import *
import requests

def get_quote():
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    kanye_quote = data["quote"]  
    canvas.itemconfig(quote_text, text=kanye_quote)
    
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg="#F0F0F0")

canvas = Canvas(width=300, height=414, bg="#F0F0F0", highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

get_quote()

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote,  borderwidth=0, activebackground="#F0F0F0", bg="#F0F0F0")
kanye_button.grid(row=1, column=0)

window.mainloop()