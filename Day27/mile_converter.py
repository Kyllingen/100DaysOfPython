# Simple app to convert miles to KM

from tkinter import *

# function to calculate
def button_clicked():
    mile = input.get()
    km = float(mile) * 1.60934
    converted_label.config(text=f"{km}")
    

#Create a window with tkinter
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

# Create input field
input = Entry(width=10)
input.grid(column=1, row=0)


# Create labels
miles_label = Label(text="Miles", padx=5)
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", justify="right", padx=5)
equal_label.grid(column=0, row=1)

converted_label = Label(text="0", justify="center")
converted_label.grid(column=1,row=1)
converted_label.config(padx=5, pady=5)

km_label = Label(text="Km", padx=5)
km_label.grid(column=2,row=1)

#Create button
button = Button(text="Calculate", justify="center", command=button_clicked)
button.grid(column=1,row=2)



window.mainloop()