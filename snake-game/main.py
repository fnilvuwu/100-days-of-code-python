from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
#need to disable tracer so that the screen don't updated by itself
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    #this fixes the graphical issue when the snake move, instead of showing every process and update the screen all the time
    #we skip it, then update the screen and put it into a 0.1 second delay before running the next line
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.all_turtles[0].distance(food) < 15:
        food.respawn()
        snake.extend()
        scoreboard.score += 1
        scoreboard.calculate_score()

    #detect collision with wall
    if snake.all_turtles[0].xcor() > 280 or snake.all_turtles[0].xcor() < -280 or snake.all_turtles[0].ycor() > 280 or snake.all_turtles[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()
        
    #detect collision with tail
    for turtle in snake.all_turtles[1:]:
        if snake.all_turtles[0].distance(turtle) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()