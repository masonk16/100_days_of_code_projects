from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
# timmy.pensize(10)
timmy.speed("fastest")
screen.colormode(255)
angles = [0, 180, 90, 270]

# def draw_shape(sides):
#     angle = 360 / sides
#
#     for i in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_sides in range(3, 11):
#     timmy.pencolor(random.randint(0, 255),
#                    random.randint(0, 255),
#                    random.randint(0, 255))
#     draw_shape(shape_sides)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r, g, b)
    return colours

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.pencolor(random_colour())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 5)

draw_spirograph(5)

screen.exitonclick()
