from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        '''constructer'''
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        
        self.left_score = 0
        self.right_score = 0
        
        
    def update_scoreboard(self):
        ''' update scoreboard'''
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
         
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))
       
    def update_score_right(self):
        '''update score right'''
        self.right_score += 1
        self.update_scoreboard()
        
    def update_score_left(self):
        '''update score for left'''
        self.left_score += 1
        self.update_scoreboard()