from tkinter import *
import pandas
import random

#Variables
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
BLACK = "#000000"

timer = None
record = None
word_list = None


# ---------------------------- SETUP DATA --------------------------------- #
def read_start_file():
    ''' reads in the most relevant file'''
    csv = None
    try:
        csv = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        csv = pandas.read_csv("data/french_words.csv")
    
    word_list = csv.to_dict(orient="records")
    return word_list

def update_words_file():
    ''' writes to words to learn file'''
    data = pandas.DataFrame(word_list)
    data.to_csv("data/words_to_learn.csv", index=False)
# ---------------------------- SELECT CARDS ------------------------------- #
def remove_card():
    '''removes the current record'''
    if len(word_list) > 0:
        word_list.remove(record)
        window.after_cancel(timer)
        
    update_words_file()
        
    select_card()
    
    
def select_card():
    ''' randomly select a card'''
    #No more words
    if len(word_list) == 0:
        canvas.itemconfig(language_text, text="No more Words", fill=BLACK)
        return
    
    global record
    record = random.choice(word_list)
    
    foreign_word = record["French"]
    
    canvas.itemconfig(card, image=front_card)
    canvas.itemconfig(language_text, text="French", fill=BLACK)
    canvas.itemconfig(word_text, text=f"{foreign_word}", fill=BLACK)
    
    global timer
    timer = window.after(3000, flip_card)    

def flip_card():
    '''flips card and shows translated word'''
    canvas.itemconfig(card, image=back_card)
    
    window.after_cancel(timer)
    
    translated_word = record["English"]
    canvas.itemconfig(language_text, text="English", fill=WHITE)
    canvas.itemconfig(word_text, text=f"{translated_word}", fill=WHITE)

# ---------------------------- UI SETUP ------------------------------- #

word_list = read_start_file()

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=front_card)

language_text = canvas.create_text((400, 150), text="French", font=("Arial", 40, "italic"), justify="center")
word_text = canvas.create_text((400, 263), text="Text", font=("Arial", 60, "bold"), justify="center")
select_card()

canvas.grid(column=0, columnspan=2, row=0)

#Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, border=0, command=remove_card)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, border=0, command=select_card)
wrong_button.grid(column=0, row=1)


window.mainloop()