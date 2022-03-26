from turtle import Screen
import time
from Models.Snake import Snake
from Models.Food import Food
from Models.ScoreBoard import ScoreBoard


def create_screen():
    screen = Screen()
    screen.setup(width=600, height=600,)
    screen.bgcolor("black")
    screen.title("My Snake Game in Python")
    screen.tracer(0)
    return screen


if __name__ == '__main__':

    screen = create_screen()
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()
    screen.listen()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

#///////////////////////Detect collision with food//////////////////////////////
        if snake.head.distance(food) < 15:
            print("hey")
            scoreboard.increase_points()
            snake.increase_snake()
            snake.change_snake_color()
            food.refresh()
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()

        for turtle in snake.turtles[1:-1]:
            if snake.head.distance(turtle) < 10:
                scoreboard.reset()
                snake.reset()


    screen.exitonclick()

