from turtle import Turtle, Screen
from snake import Snake
import time

snake = None
screen = None
game_is_on = True

def initialize_screen():
    ''' initializes the screen'''
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    
    return screen


# move the snake

# create a snake food

#detect collision with food

# create a scoreboard

#detect collision with wall

# detect collision with tail

screen = initialize_screen()

snake = Snake()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()


screen.exitonclick()
