from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

play_game = True
while play_game:
    screen.update()
    time.sleep(1)

    snake.move()


screen.exitonclick()
