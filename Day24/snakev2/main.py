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
current_speed = 0.1

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


while game_is_on:
    screen.update()
    time.sleep(current_speed)
    
    snake.move()
    
    # detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh() 
        snake.extend()
        scoreboard.update_score()
    
        # increase speed every 5 food
        if (scoreboard.get_score() % 5) == 0:
            current_speed = current_speed - 0.01
        
    # detect collision with wall
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 \
          or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        scoreboard.reset_score() 
        snake.reset()
        
    # detect collision with tail 
    for segment in snake.snake[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset()
    

screen.exitonclick()
