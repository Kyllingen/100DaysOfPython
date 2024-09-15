from turtle import Turtle

class Paddle(Turtle):
    
    MOVE_STEP = 20
    
    def __init__(self, starting_pos):
        ''' create the paddle and position it'''
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_pos[0], starting_pos[1])
        self.showturtle()
        
    def up(self):
        ''' move padle up MOVE_STEP units'''
        if self.ycor() + 50 < 300:
            self.goto(self.xcor(), self.ycor()+self.MOVE_STEP)
    
    def down(self):
        ''' move padle up MOVE_STEP units'''
        if self.ycor() - 50 > -300:
            self.goto(self.xcor(), self.ycor()-self.MOVE_STEP)