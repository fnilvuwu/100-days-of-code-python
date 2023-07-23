from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, starting_position):
        #super().__init__() is basically the same as self = Turtle()
        #what it do is that it will initialize the super class
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_position)

    def move_up(self):
        self.sety(self.ycor() + 20)

    def move_down(self):
        self.sety(self.ycor() - 20)

