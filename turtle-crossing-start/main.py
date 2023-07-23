import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")


scoreboard = Scoreboard()

car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    #won condition
    if player.ycor() > 280:
        scoreboard.user_won()
        player.reset_position()
        car.level_up()

    #collision with car
    for cars in car.all_cars:
        if player.distance(cars) < 20:
            scoreboard.game_over()
            game_is_on = False

    

screen.exitonclick()

