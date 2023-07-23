import turtle
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("Guess U.S. States Game")
screen.addshape("blank_states_img.gif")

turtle.shape("blank_states_img.gif")

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    user_answer = screen.textinput(title=f"{scoreboard.correct_answer}/{scoreboard.answer_to_guess} State", prompt="Enter a state name").title()
    if user_answer == "Exit":
        scoreboard.missing_state()
        break
    scoreboard.check_answer(user_answer)


screen.exitonclick()