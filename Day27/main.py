import tkinter

#Create a window with tkinter
window = tkinter.Tk()

window.title("First GUI program")
window.minsize(width=500, height=300)

# create components 
## Label
label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
label.pack()

# different ways to update text
label["text"] = "New Text"
label.config(text="Updated text")

# Create button
def button_clicked():
    label["text"] = input.get()

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

#Entry (Input) 
input = tkinter.Entry(width=10)
input.insert(tkinter.END, "Some starting text")
input.pack()

#Text
text = tkinter.Text(height=5, width=30)
text.focus()
text.insert(tkinter.END, chars="Example of multi-line text entry")
text.pack()

#Spinbox
def spinbox_used():
    print(spinbox.get())
    
spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
def scale_used():
    print(scale.get())
scale = tkinter.Scale(from_=0, to=100, width=5, command=scale_used)
scale.pack()

#Checkbox
def checkbox_used():
    print(check_state.get())
    
check_state = tkinter.IntVar()
checkbox = tkinter.Checkbutton(text="Is On?", variable=check_state, command=checkbox_used)
checkbox.pack()

#Radio button
def radio_button_used():
    print(radio_state.get())
    
radio_state = tkinter.IntVar()
radio_button1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_button_used)
radio_button2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_button_used)
radio_button1.pack()
radio_button2.pack()

#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListBoxSelector>>", listbox_used)
listbox.pack()

window.mainloop()