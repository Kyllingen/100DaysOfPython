from turtle import Turtle

class Paddle:
    
    paddle = None
    MOVE_STEP = 20
    
    def __init__(self):
        ''' create the paddle and position it'''
        self.paddle = Turtle(shape="square")
        self.paddle.hideturtle()
        self.paddle.color("white")
        self.paddle.turtlesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(350, 0)
        self.paddle.showturtle()
        
    def up(self):
        ''' move padle up MOVE_STEP units'''
        if self.paddle.ycor() + 50 < 300:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor()+self.MOVE_STEP)
    
    def down(self):
        ''' move padle up MOVE_STEP units'''
        if self.paddle.ycor() - 50 > -300:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor()-self.MOVE_STEP)