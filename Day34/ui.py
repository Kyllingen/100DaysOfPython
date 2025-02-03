
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        '''Constructor'''
        
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=340, height=500, padx=20, pady=20, bg=THEME_COLOR)

        # score
        self.score = Label(text="Score: 0", fg=WHITE, font=("Arial", 10), bg=THEME_COLOR, justify="center")
        self.score.grid(column=1, row=0)
        self.score.grid_columnconfigure(1, weight=1)
        
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg=WHITE, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Starting Text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        #Buttons
        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, border=0, padx=20, pady=20)
        self.right_button.grid(column=0, row=2, padx=20)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, border=0, padx=20, pady=20)
        self.wrong_button.grid(column=1, row=2, padx= 20)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        '''gets next question'''
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
    