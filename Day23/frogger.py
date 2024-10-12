from turtle import Turtle

class Frogger(Turtle):
    
    TURTLE_STARTING_POINT_Y = -230
    TURTLE_ENDING_POINT_Y = 250
    
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.reset_turtle()
        
        
    def reset_turtle(self):
        '''resets turtle to starting point'''
        self.goto(0,self.TURTLE_STARTING_POINT_Y)
        
    def up(self):
        '''move turtle up'''
        self.forward(8)
        
    def reset_position(self):
        '''sets turtle back to starting position'''
        self.setpos(self.xcor(), self.TURTLE_STARTING_POINT_Y)