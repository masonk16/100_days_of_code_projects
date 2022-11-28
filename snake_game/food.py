from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pen()
        self.pensize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        random_x = random.randint(-290, 290)
        random_y = random.randint(-290, 290)
        self.goto(random_x, random_y)
