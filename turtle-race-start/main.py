from turtle import Turtle, Screen
from random import randint

my_screen = Screen()
my_screen.setup(width=400, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
race_going = False

x=-150
y=-150
for i in range(5):
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(colors[i])
    my_turtle.penup()
    my_turtle.goto(x, y)
    all_turtles.append(my_turtle)
    y += 75

if user_bet:
    race_going = True

while race_going:
    for turtle in all_turtles:
        if turtle.xcor() >= 150:
            race_going = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"Congrats! The {winning_turtle} turtle have won the race, You won $100.000")
            else:
                print(f"Oopsie! The {winning_turtle} turtle have won the race, You lost your bet")

        speed = randint(0,10)
        turtle.forward(speed) 

my_screen.exitonclick()