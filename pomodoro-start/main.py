from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Bebas Neue"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
work_rep = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    check_icon.config(text="")
    timer_label.config(fg=GREEN, text="Timer", bg=YELLOW, font=(FONT_NAME, 50))
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global work_rep
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down(3)
        timer_label.config(fg=RED, text="Break", bg=YELLOW, font=(FONT_NAME, 50))
    elif reps > 8:
        reset_timer()
    elif reps % 2 == 0:
        count_down(3)
        timer_label.config(fg=PINK, text="Break", bg=YELLOW, font=(FONT_NAME, 50))
    else:
        count_down(3)
        timer_label.config(fg=GREEN, text="Focus", bg=YELLOW, font=(FONT_NAME, 50))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for n in range(work_sessions):
            marks += "✔"
        check_icon.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



timer_label = Label(fg=GREEN, text="Timer", bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)


check_icon = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
check_icon.grid(row=3, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "normal"))
canvas.grid(row=1, column=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)




window.mainloop()
