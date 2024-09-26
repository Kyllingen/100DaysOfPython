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
        
        #set initial heading NE
        angle = self.towards(300,300)
        #self.setheading(angle)
        
        
    def move(self):
        '''move the ball'''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce(self, hit_paddle=False):
        '''bounces and changes direction'''
        added_change = random.randint(-2, 2)
        if hit_paddle:
            self.x_move =- self.x_move + added_change
        else:
            self.y_move =- self.y_move + added_change
        