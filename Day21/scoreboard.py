 
from turtle import Turtle

ALIGN="center"
FONT=("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    score = -1
    
    def __init__(self):
        ''' initializes the scoreboard'''
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        ''' updates the score text'''
        self.clear()
        self.score += 1
        self.goto(x = 0, y = 260)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        
    def game_over(self):
        ''' displays game over text'''
        self.goto(x = 0, y = 0)
        self.write("Game Over", align=ALIGN, font=FONT)
        
    def get_score(self):
        ''' get current score'''
        return self.score
        
        