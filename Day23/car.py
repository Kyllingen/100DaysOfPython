from turtle import Turtle
import random

class Car(Turtle):
    
    def __init__(self, speed):
        ''' constructor'''
        super().__init__()
        
        self.penup()
        self.shape("square")
        self.car_speed = speed
        
        r = random.random()
        g = random.random()
        b = random.random()
        self.color((r,g,b))
                
        self.shapesize(stretch_wid=0.9, stretch_len=1.8)
        self.setheading(180)
        
        y_position = random.randrange(-190,250,40)
        x_offset = random.randint(1,200)
        self.goto(300 + x_offset, y_position)
        
    def move(self):
        '''move car'''
        self.forward(self.car_speed)
        
    def set_speed(self, new_speed):
        ''' sets a new speed on car'''
        self.car_speed = new_speed