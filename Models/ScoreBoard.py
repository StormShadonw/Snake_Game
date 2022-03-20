from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        style = ('Courier', 22, 'italic')
        self.goto(0, 250)
        self.write("Score: " + str(self.points), False, align="Center", font=style)

    def increase_points(self):
        self.points += 1
        self.clear()
        style = ('Courier', 22, 'italic')
        self.write("Score: " + str(self.points), False, align="Center", font=style)

    def game_over(self):
        style = ('Courier', 22, 'italic')
        self.goto(0, 0)
        self.write("GAME OVER", False, align="Center", font=style)

