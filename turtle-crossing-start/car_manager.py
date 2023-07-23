from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE   

    def create_car(self):
        spawn_chance = randint(1, 6)
        if spawn_chance == 1:
            new_car = Turtle()
            new_car.color(choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.goto(cars.xcor() - self.car_speed, cars.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT



        

    
