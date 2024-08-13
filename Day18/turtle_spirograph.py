from turtle import Turtle, Screen
import random

RADIUS = 100
CIRCLES = 36
tim = Turtle()
tim.speed(0)

def set_random_color():
    ''' sets a random color'''
    tim.color((random.random(), random.random(), random.random()))
    
# draw random walk for circles steps
for _ in range(CIRCLES):
    set_random_color()    
    tim.circle(RADIUS)
    tim.setheading(tim.heading() + 360/CIRCLES)

screen = Screen()
screen.exitonclick()