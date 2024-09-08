#rainbow turtles
# move from left to right randomly

from turtle import Turtle, Screen
import random

screen = None
turtles = []
RAINBOW_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
GOAL_LINE = 270

def initialize():
    ''' initializes the screen and the turtles'''
    
    screen = Screen()
    screen.setup(width=600, height=400)

    for i in range(len(RAINBOW_COLORS)):
        turtle = Turtle(shape="turtle")
        turtle.color(RAINBOW_COLORS[i])
        turtle.penup()
        turtle.goto(x = -280, y = -100 + i * 40)
        turtles.append(turtle)
        
    ''' sets the goal line'''
    goal = Turtle()
    goal.penup()
    goal.goto(x = GOAL_LINE, y = 200)
    goal.pendown()
    goal.goto(x = GOAL_LINE, y = -200)
    goal.hideturtle()
    
    return screen
        
def bet_on_turtle():
    ''' takes the user's bet'''
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    return user_bet

def move_turtles():
    ''' moves the turtles randomly'''
    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance) 
        
def race_over(user_bet):
    ''' checks if the user's bet is correct'''
    for turtle in turtles:
        if turtle.xcor() > GOAL_LINE:
            if turtle.color()[0] == user_bet:
                print("You won!")
            else:
                print("You lost!")
            return True
    return False

def start_race():
    ''' starts the race'''
    user_bet = bet_on_turtle()
    
    while not race_over(user_bet):
        move_turtles()
        

# initialize the screen and the turtles
screen = initialize()
print(screen)
# start the race
start_race()

screen.exitonclick()    


    
