from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from middle_line import MiddleLine
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")

screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

ball = Ball()
scoreboard = Scoreboard() 
middle_line = MiddleLine()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    
    screen.update()
    ball.move()
    
    #collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()

    #ball out of bound
    if ball.xcor() > 400:
        ball.reset()
        ball.bounce_x()
        scoreboard.l_scored()
        
    if ball.xcor() < -400:
        ball.reset()
        ball.bounce_x()
        scoreboard.r_scored()

screen.exitonclick()