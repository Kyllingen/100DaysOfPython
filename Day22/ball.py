from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self):
        ''' initialize the ball'''
        super().__init__()
        
        self.shape("circle")
        self.color("white")
        self.penup()
        
        #set initial heading NE
        angle = self.towards(300,300)
        self.setheading(angle)
        
        
    def move(self):
        '''move the ball'''
        self.forward(15)
        
    def bounce(self):
        '''bounces and changes direction'''
        current_angle = self.heading()
        random_add = random.randint(-5, 5)
        current_angle += random_add
        
        if current_angle >= 0 and current_angle < 90:
            self.setheading(current_angle-90)
        elif current_angle >= 90 and current_angle < 180:
            self.setheading(current_angle+90)
        elif current_angle >= 180 and current_angle < 270:
            self.setheading(current_angle-90)
        else:
            self.setheading(current_angle+90-360)
        
        