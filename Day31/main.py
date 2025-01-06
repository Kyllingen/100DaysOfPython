from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flasg Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

image_logo = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=image_logo)

canvas.create_text((400, 150), text="text", font="Arial 40 italic", justify="center")
canvas.create_text((400, 263), text="Bigger", font="Arial 60 bold", justify="center")
canvas.grid(column=0, columnspan=2, row=0)

#Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, border=0)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, border=0)
wrong_button.grid(column=0, row=1)


window.mainloop()