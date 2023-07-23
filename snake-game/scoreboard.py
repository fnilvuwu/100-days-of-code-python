from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.write(f"Score : {self.score} High Score : {self.high_score}",
                   align="center", font=("Arial", 24, "normal"))

    def calculate_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}",
                   align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highest_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.calculate_score()
