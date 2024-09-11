 
from turtle import Turtle

class Scoreboard(Turtle):
    
    score = -1
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.score += 1
        self.goto(x = 0, y = 260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        
        