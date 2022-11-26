from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colours[turtle_index])
    tim.penup()
    tim.goto(x=-235, y=y_position[turtle_index])


if user_bet:
    race_on = True

while race_on:
    random_distance = random.randint(0, 15)
    



screen.exitonclick()
