from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    checkmark.config(text="")
    header.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    
    
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    ''' Starts timer for next rep'''
    global reps 
    
    reps += 1
    
    if reps == 8:
        countdown(LONG_BREAK_MIN*60)
        header.config(text="Break", fg=RED)
    elif (reps % 2) == 0:
        countdown(SHORT_BREAK_MIN*60)
        header.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN*60)
        header.config(text="Work", fg=GREEN)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    seconds = count % 60
    minutes = math.floor(count / 60)
    
    if seconds < 10:
        seconds = "0" + str(seconds)
    
    counter = f'{minutes}:{seconds}'
    
    canvas.itemconfig(timer_text, text=counter)
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        
        if reps % 2 == 0:
            checks = checkmark["text"]
            checks += "✔"
            checkmark.config(text=checks)
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Header
header = Label(text="Timer", font=(FONT_NAME, 46, "bold"))
header.config(fg=GREEN, justify="center", bg=YELLOW)
header.grid(column=1,row=0)

#Buttons
start_button = Button(text="Start", justify="right", highlightthickness=0, command=start_timer)
reset_button = Button(text="Reset", justify="left", highlightthickness=0, command=reset_timer)
start_button.grid(column=0,row=2)
reset_button.grid(column=2,row=2)

#checkmark label
checkmark = Label(text="", fg=GREEN, bg=YELLOW, justify="center", font=(FONT_NAME, 12))
checkmark.grid(column=1,row=3)



window.mainloop()