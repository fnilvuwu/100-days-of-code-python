from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 250)   
        self.user_score = 1
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.user_score}", align="left", font=FONT)

    def user_won(self):
        self.user_score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
