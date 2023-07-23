from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__ (self):
        self.all_turtles = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_turtles(position)

    def add_turtles(self, position):
        my_turtle = Turtle()
        my_turtle.color("white")
        my_turtle.shape("square")
        my_turtle.penup()
        my_turtle.goto(position)
        self.all_turtles.append(my_turtle)
        
    def extend (self):
        self.add_turtles(self.all_turtles[-1].position())


    def move (self):
        #this will make the snake to folow it's head, all_turtle[3] will follow all_turtle[2] and so forth
        for turtle_num in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[turtle_num - 1].xcor()
            new_y = self.all_turtles[turtle_num - 1].ycor()
            self.all_turtles[turtle_num].goto(new_x, new_y)
        self.all_turtles[0].forward(MOVE_DISTANCE)

    def up (self):
        if self.all_turtles[0].heading() != DOWN:
            self.all_turtles[0].setheading(UP)

    def down (self):
        if self.all_turtles[0].heading() != UP:
            self.all_turtles[0].setheading(DOWN)
    
    def left (self):
        if self.all_turtles[0].heading() != RIGHT:
            self.all_turtles[0].setheading(LEFT)

    def right (self):
        if self.all_turtles[0].heading() != LEFT:
            self.all_turtles[0].setheading(RIGHT)
        
    def reset (self):
        for i in self.all_turtles:
            i.reset()
        self.all_turtles.clear()
        self.create_snake()
