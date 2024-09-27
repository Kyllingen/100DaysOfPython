from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self):
        ''' initialize the ball'''
        super().__init__()
        
        self.shape("circle")
        self.color("white")
        self.penup()
        
        self.x_move = 10
        self.y_move = 10
        
        self.move_speed = 0.1
        
        #set initial heading NE
        self.towards(300,300)
        
        
    def move(self):
        '''move the ball'''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce(self, hit_paddle=False):
        '''bounces and changes direction'''

        if hit_paddle:
            self.x_move = -self.x_move 
            self.move_speed *= 0.9
        else:
            self.y_move = -self.y_move 
        
    def reset(self):
        '''reset ball and send ball in opposite direction'''
        self.setposition(0,0)
        self.x_move = -self.x_move
        self.move_speed = 0.1