from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

positions = [(-20, 0), (0, 0), (20, 0)]

segments = []
for position in positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)



play_game = True
while play_game:
    screen.update()
    time.sleep(1)
    for seg in segments:
        seg.forward(20)

screen.exitonclick()
