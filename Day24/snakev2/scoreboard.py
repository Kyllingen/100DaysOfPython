 
from turtle import Turtle

ALIGN="center"
FONT=("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        ''' initializes the scoreboard'''
        super().__init__()
        
        #read high score from file. 
        #Assume file exists and only contains an int
        with open("data.txt") as file:
            self.high_score = int(file.read())
        
        self.score = -1
        
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
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)
        
    def reset_score(self):
        ''' check for high score and reset'''
        if self.score > self.high_score:
            self.high_score = self.score
            
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        
        self.score = -1
        self.update_score()
        
    def get_score(self):
        ''' get current score'''
        return self.score
        
        