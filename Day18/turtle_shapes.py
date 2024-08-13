from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("coral")

# Draw different shapes un different colors
for i in range(3, 20):
    tim.color(random.random(), random.random(), random.random())
    for _ in range(i):
        tim.forward(100)
        tim.right(360/i)

screen = Screen()
screen.exitonclick()