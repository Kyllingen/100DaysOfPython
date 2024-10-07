#Imports
from turtle import Screen,Turtle
from frogger import Frogger
from car import Car
import time

# definitions
screen = None
game_on = True

def init_screen():
    ''' initalizes screen parameters'''
    screen = Screen()
    screen.bgcolor("white")
    screen.setup(width=600, height=600)
    screen.title("Crossing Game")
    screen.tracer(0)
    
    return screen

def draw_lanes():
    ''' draws the car lanes'''
    painter = Turtle()
    painter.hideturtle()
    painter.color("gray")
    painter.pensize(5)
    
    painter.penup()
    painter.goto(-300, -210)
    painter.pendown()
    painter.goto(300, -210)
    painter.penup()
    
    painter.penup()
    painter.goto(-300, 230)
    painter.pendown()
    painter.goto(300, 230)
    painter.penup()
    
    painter.color("yellow")
    painter.pensize(2)
    
    for i in range(-170, 210, 40):
        painter.goto(-300,i)
        painter.pendown()
        painter.goto(300,i)
        painter.penup()
    
    
 
# initialize objects   
screen = init_screen()
draw_lanes()
screen.listen()

frogger = Frogger()
screen.onkey(key="Up", fun=frogger.up)

# create a set of cars to start off screen at random "lanes"
cars = []
for i in range(1,20):
    cars.append(Car())

# Game loop
while game_on: 
    screen.update()
    time.sleep(0.6)
    
    #move all cars
    for i in range(0, len(cars)):
        cars[i].move()
        
        if cars[i].xcor() < -330:
            cars.remove(cars[i])

screen.exitonclick()