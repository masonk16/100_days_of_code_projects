from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Snake Game")

x_position = [-20, 0, 20]
for x in x_position:
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=x, y=0)


screen.exitonclick()
