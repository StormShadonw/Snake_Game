from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, 280)
        self.write("Score: ", False, align="Center")
