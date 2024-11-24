from tkinter import * 

# functions
def button_clicked():
    label["text"] = input.get()
    

#Create a window with tkinter
window = Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# create components 
## Label
label = Label(text="Label", font=("Arial", 24, "bold"))
label.config(text="New Text")
label.config(padx=10, pady=10)

# Different layout managers
#label.pack()
#label.place(x=0, y=0)
label.grid(column=0, row=0)

# Create button
button = Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

#create another button
button2 = Button(text="New Button", command=button_clicked)
button2.grid(column=2,row=0)

#Entry
input = Entry(width=10)
#input.pack()
input.grid(column=3, row=2)



window.mainloop()