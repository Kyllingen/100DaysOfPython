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

# create a snake food

#detect collision with food

# create a scoreboard

#detect collision with wall

# detect collision with tail

screen = initialize_screen()

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()


screen.exitonclick()
