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

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)







screen.exitonclick()
