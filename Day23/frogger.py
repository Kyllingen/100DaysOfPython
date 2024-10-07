from turtle import Turtle

class Frogger(Turtle):
    
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(0,-230)
        
    def up(self):
        '''move turtle up'''
        self.forward(40)