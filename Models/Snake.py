from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in POSITIONS:
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(position)
            self.turtles.append(turtle)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for turtle_index in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle_index - 1].xcor()
            new_y = self.turtles[turtle_index - 1].ycor()
            self.turtles[turtle_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


