import turtle
import pandas

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()
class Scoreboard:

    def __init__(self):
        self.correct_answer = 0
        self.answer_to_guess = len(data["state"].to_list())
        

    def check_answer(self, user_answer):
        for states in state_list:
            if user_answer == states:
                state_list.remove(states)
                self.correct_answer += 1
                search_state = data[data["state"] == f"{states}"]
                x_cor = int(search_state["x"])
                y_cor = int(search_state["y"])
                turtle.goto(x_cor, y_cor)
                turtle.write(f"{states}", align="center", font=('Arial', 10, 'bold'))

    def missing_state(self):
        data = pandas.DataFrame(state_list)
        data.to_csv("not_guessed_state.csv")