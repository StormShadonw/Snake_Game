from turtle import Turtle
import random

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
COLORS = ["red", "green", "yellow", "orange", "purple", "blue", "white"]

class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in POSITIONS:
            self.extend_snake(position)

    def increase_snake(self):
        final_x_position = self.turtles[-1].xcor()
        final_y_position = self.turtles[-1].ycor()
        self.extend_snake((final_x_position - 20, final_y_position))

    def change_snake_color(self):
        random_number = random.randint(0, len(COLORS) - 1)
        for turtle in self.turtles:
            turtle.color(COLORS[random_number])

    def extend_snake(self, position):
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


