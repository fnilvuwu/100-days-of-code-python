from turtle import Turtle
import random

#fixed the food not being in line with snake
food_location = []
for i in range(-280, 281):
    if i % 20 == 0:
        food_location.append(i)

class Food(Turtle):



    def __init__ (self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.respawn()

    def respawn(self):
        random_x = random.choice(food_location)
        random_y = random.choice(food_location)
        self.goto(random_x, random_y)