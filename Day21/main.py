from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def initialize_screen():
    ''' initializes the screen'''
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    
    return screen

#detect collision with wall

# detect collision with tail


game_is_on = True
screen = initialize_screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    # detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh() 
        scoreboard.update_score()   


screen.exitonclick()
