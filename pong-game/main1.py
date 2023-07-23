from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(1200, 600)
screen.bgcolor("black")
screen.listen()
player1_score = 0
player2_score = 0

x1=-550
x2=550
y1=0
y2=0
def go_up():
    global y1
    y1 += 10
    paddle_one.goto(x1, y1)

def go_down():
    global y1
    y1 -= 10
    paddle_one.goto(x1, y1)

def go_up2():
    global y2
    y2 += 10
    paddle_two.goto(x2, y2)

def go_down2():
    global y2
    y2 -= 10
    paddle_two.goto(x2, y2)

paddle_one = Turtle()
paddle_one.color("white")
paddle_one.penup()
paddle_one.shapesize(stretch_wid=4, stretch_len=1)
paddle_one.shape("square")
paddle_one.goto(x1, y1)
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

paddle_two = Turtle()
paddle_two.color("white")
paddle_two.penup()
paddle_two.shapesize(stretch_wid=4, stretch_len=1)
paddle_two.shape("square")
paddle_two.goto(x2, y2)
screen.onkey(go_up2, "w")
screen.onkey(go_down2, "s")

ball = Turtle()
ball.color("white")
ball.shape("circle")
ball.penup()
ball_heading = 135
ball.setheading(ball_heading)

score1 = Turtle()
score1.color("white")
score1.hideturtle()
score1.penup()
score1.goto(-100, 220)
score1.write(player1_score, align="center", font=("Arial", 40, "normal"))

score2 = Turtle()
score2.color("white")
score2.hideturtle()
score2.penup()
score2.goto(100, 220)
score2.write(player2_score, align="center", font=("Arial", 40, "normal"))

while ball_heading == 90 or ball_heading == 270:
    ball_heading = randint(0, 360)
    ball.setheading(ball_heading)

game_is_on = True
while game_is_on:
    ball.forward(4)
    if ball.ycor() > 200 or ball.ycor() < -200:
        if ball_heading < 90 and ball_heading > 0 or ball_heading < 270 and ball_heading > 180: 
            ball_heading += 270
        elif ball_heading < 360 and ball_heading > 270 or ball_heading < 180 and ball_heading > 90: 
            ball_heading += 90

        if ball_heading > 360:
            ball_heading %= 360
        
        print(ball_heading)
        ball.setheading(ball_heading)
    
    if ball.distance(paddle_one) < 20 or ball.distance(paddle_two) < 20:
        ball_heading += 180
        ball.setheading(ball_heading)

        if ball_heading > 360:
            ball_heading %= 360

    if ball.xcor() > 600:
        ball.goto(0, 0)
        player1_score += 1
        score1.clear()
        score1.write(player1_score, align="center", font=("Arial", 40, "normal"))
    elif ball.xcor() < -600:
        ball.goto(0, 0)
        player2_score += 1
        score2.clear()
        score2.write(player2_score, align="center", font=("Arial", 40, "normal"))
        
        

screen.exitonclick()