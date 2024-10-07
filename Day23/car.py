from turtle import Turtle
import random

class Car(Turtle):
    
    def __init__(self):
        ''' constructor'''
        super().__init__()
        
        self.penup()
        self.shape("square")
        
        r = random.random()
        g = random.random()
        b = random.random()
        self.color((r,g,b))
                
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        
        y_position = random.randrange(-190,250,40)
        x_offset = random.randint(1,200)
        self.goto(300 + x_offset, y_position)
        
    def move(self):
        '''move car'''
        self.forward(40)