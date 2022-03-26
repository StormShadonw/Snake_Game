from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.high_score = self.read_file()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        style = ('Courier', 22, 'italic')
        self.goto(0, 250)
        self.update()

    def increase_points(self):
        self.points += 1
        self.update()

    # def game_over(self):
    #     style = ('Courier', 22, 'italic')
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align="Center", font=style)

    def update(self):
        self.clear()
        style = ('Courier', 22, 'italic')
        self.write(f"Score: {self.points} High Score: {self.read_file()}", False, align="Center", font=style)

    def read_file(self):
        with open("data.txt") as file:
            data = file.read()
        return int(data)

    def write_file(self, points):
        with open("data.txt", "w") as file:
            file.write(points)

    def reset(self):
        if self.points > self.read_file():
            self.write_file(str(self.points))
        self.points = 0
        self.update()

