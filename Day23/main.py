#Imports
from turtle import Screen,Turtle
from frogger import Frogger
from car_manager import CarManager
from scoreboard import Scoreboard
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

# init car manager
car_manager = CarManager()
car_counter = 1

# init scoreboard
score_board = Scoreboard()
score_board.update_scoreboard()

# Game loop
while game_on: 
    time.sleep(0.1)
    screen.update()
    
    #create new car every n'th iteration
    car_counter += 1
    if car_counter == CarManager.CAR_CREATE_ITERATION:
        car_manager.create_car()
        car_counter = 1
    
    #move all cars
    car_manager.move_cars()
    
    # check for collision
    collided = car_manager.check_collision(frogger)
    if collided:
        score_board.game_over()
        break
    
    # increase speed on cars and reset frogger
    if frogger.ycor() >= Frogger.TURTLE_ENDING_POINT_Y:
        frogger.reset_position()
        car_manager.increase_speed()
        score_board.update_scoreboard()
    

screen.exitonclick()