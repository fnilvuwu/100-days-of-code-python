from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)    

        self.question_canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.question_canvas.create_text(150, 125, width=280, font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=(20))
        self.score_label.grid(column=1, row=0)
        
        true_image = PhotoImage(file="images/true.png")
        self.true_input = Button(image=true_image, borderwidth=0, command=self.true_pressed)
        self.true_input.grid(column=0, row=2)
# 
        false_image = PhotoImage(file="images/false.png")
        self.false_input = Button(image=false_image, borderwidth=0, command=self.false_pressed)
        self.false_input.grid(column=1, row=2)
        # self.question_canvas
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_input.config(state="disabled")
            self.false_input.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
