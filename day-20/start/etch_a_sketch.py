from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    """"Moves turtle forwards"""
    tim.forward(10)


def move_backward():
    """Moves turtle backwards"""
    tim.backward(10)


def turn_left():
    """Turns turtle counter-clockwise"""
    tim.setheading(tim.heading() + 10)


def turn_right():
    """Turns turtle clockwise"""
    tim.right(10)


def clear_screen():
    """Clears drawing and resets turtle to center"""
    tim.reset()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()
