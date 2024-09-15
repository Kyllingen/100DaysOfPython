from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        ''' initialize the ball'''
        super().__init__()
        
        self.shape("circle")
        self.color("white")
        self.penup()
        
        #set initial heading NE
        angle = self.towards(400,300)
        self.setheading(angle)
        
        
    def move(self):
        '''move the ball'''
        self.forward(15)
        