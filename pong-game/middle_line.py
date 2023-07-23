from turtle import Turtle

class MiddleLine(Turtle):

    def __init__(self):
        super().__init__()
        #i is the space of each line drawn
        i = 6
        start = 300
        self.color("white")
        self.hideturtle()
        self.penup()
        for x in range(50):
            self.goto(0, start)
            self.pendown()
            start -= i
            self.goto(0, start)
            self.penup()
            start -= i

    # def draw_middle_line(self):
        