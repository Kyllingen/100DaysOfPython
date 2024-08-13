from turtle import Turtle, Screen
import random

STEP_SIZE = 20
tim = Turtle()
tim.pensize(15)
tim.speed(0)

def set_random_color():
    ''' sets a random color'''
    tim.color((random.random(), random.random(), random.random()))

def set_random_direction():
    ''' sets a random direction in 90 degree angles'''
    tim.setheading(random.choice([0, 90, 180, 270]))
    
# draw random walk for 100 steps
for _ in range(200):
    set_random_color()
    set_random_direction()
    tim.forward(STEP_SIZE)
    

screen = Screen()
screen.exitonclick()