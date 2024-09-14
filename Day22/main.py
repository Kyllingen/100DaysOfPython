#Imports
from turtle import Turtle, Screen
from paddle import Paddle
import random
import time

# definitions
screen = None
game_on = True

def init_screen():
    ''' initalizes screen parameters'''
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong Game")
    screen.tracer(0)
    return screen

def draw_border_line(pen, x_pos, y_pos):
    ''' draws border lines at top and bottom of court'''
    pen.penup()
    pen.setposition(-x_pos,y_pos)
    pen.pendown()
    pen.goto(x_pos, y_pos)
    
def setup_court():
    '''draw the court'''
    pen = Turtle(shape="square")
    pen.hideturtle()
    pen.pencolor("white")
    pen.pensize(5)
    
    draw_border_line(pen, 400, -290)
    draw_border_line(pen, 400, 290)
    
    #draw center line
    pen.penup()
    pen.setposition(0,-300)
    for i in range(1,50):
        pen.pendown()
        pen.goto(pen.xcor(), pen.ycor()+10)
        pen.penup()
        pen.goto(pen.xcor(), pen.ycor()+10)

 
# initialize objects   
screen = init_screen()
setup_court()
paddle = Paddle()

screen.listen()
screen.onkey(key="Up", fun=paddle.up)
screen.onkey(key="Down", fun=paddle.down)


# Game loop
while game_on: 
    screen.update()
    time.sleep(0.09)
    


screen.exitonclick()