from turtle import Turtle


class PaddleOne(Turtle):
    """Instantiates the first paddle."""
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=20, stretch_len=100)
        self.color("white")
        self.penup()
        self.goto(350, 0)

