from turtle import Turtle, Screen
from paddle import PaddleOne


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.speed("fastest")
paddle.penup()
paddle.goto(350, 0)
paddle.shapesize(stretch_wid=5, stretch_len=1)

paddle.penup()
paddle.goto(350, 0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")

play_game = True
while play_game:
    screen.update()

     screen.exitonclick()

