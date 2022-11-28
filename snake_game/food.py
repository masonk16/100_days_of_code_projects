from turtle import Turtle
import random


class Food(Turtle):
    """Manages the food for the snake game."""

    def __init__(self):
        """Controls appearance of food - color, shape, size and speed."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Generates food at random points on the screen. 
        maximum y value reduced to avoid collision with scoreboard.
        """
        random_x = random.randint(-290, 290)
        random_y = random.randint(-290, 265)
        self.goto(random_x, random_y)