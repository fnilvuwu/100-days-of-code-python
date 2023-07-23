import tkinter

def button_clicked():
    to_km = int(my_input.get()) * 1.6
    my_label2.config(text=f'{format(to_km,".2f")}')

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#label
my_label = tkinter.Label(text="is equal to")
my_label.grid(column=0, row=1)

my_label2 = tkinter.Label(text="0")
my_label2.grid(column=1, row=1)

my_label3 = tkinter.Label(text="Miles")
my_label3.grid(column=3, row=0)

my_label4 = tkinter.Label(text="Km")
my_label4.grid(column=3, row=1)

#button
my_button = tkinter.Button(text="Calculate", command=button_clicked)
my_button.grid(column=1, row=2)

#entry/text input
my_input = tkinter.Entry(width=7)
my_input.grid(column=1, row=0)


window.mainloop()
