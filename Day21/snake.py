from turtle import Turtle

class Snake:
    
    snake = []
    MOVE_DISTANCE = 20
    snake_head = None
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0
    
    def __init__(self):
        ''' initializes the snake'''
        self.create_snake()
          
            
    def create_snake(self):
        ''' creates a snake with 3 segments'''
        for i in range(3):
            self.add_segment((0,0))
            
        self.snake_head = self.snake[0]
            
    def move(self):
        ''' moves the snake'''
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num-1].xcor()
            new_y = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        
        self.snake_head.forward(self.MOVE_DISTANCE) 
    
    def add_segment(self, position):
        ''' adds a segment to the snake'''
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)    
    
    def extend(self):
        ''' extends the snake with a new segment'''
        self.add_segment(self.snake[-1].position())
        
    def up(self):
        ''' moves the snake up'''
        if self.snake_head.heading() != self.DOWN:
            self.snake_head.setheading(self.UP)
    
    def down(self):
        ''' moves the snake down'''
        if self.snake_head.heading() != self.UP:
            self.snake_head.setheading(self.DOWN)
        
    def left(self):
        ''' moves the snake left'''
        if self.snake_head.heading() != self.RIGHT:
            self.snake_head.setheading(self.LEFT)
        
    def right(self):
        ''' moves the snake right'''
        if self.snake_head.heading() != self.LEFT:
            self.snake_head.setheading(self.RIGHT)