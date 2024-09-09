from turtle import Turtle

class Snake:
    
    snake = []
    DIRECTIONS = ["up", "down", "left", "right"]
    current_direction = "right"
    
    def __init__(self):
        ''' creates a snake body'''
        for i in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(x = -20 * i, y = 0)
            self.snake.append(segment)   
            
    def move(self):
        ''' moves the snake'''
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num-1].xcor()
            new_y = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        
        self.snake[0].forward(20) 