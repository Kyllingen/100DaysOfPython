from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        '''constructer'''
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        
        self.level = 0
        
        
    def update_scoreboard(self):
        ''' update level text'''
        self.clear()
        self.goto(-230, 250)
        self.level += 1
        text = "Level " + str(self.level)
        self.write(text, align="center", font=("Courier", 20, "normal"))
        
    def game_over(self):
        self.goto(-50, 0)
        text = "GAME OVER"
        self.write(text, align="center", font=("Courier", 30, "normal"))
        
