from tkinter import *
from tkinter import messagebox
import random
import pyperclip

WHITE = "#FFFFFF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    # static data for use
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    num_letters = random.randint(8,12)
    num_numbers = random.randint(2,4)
    num_symbols = random.randint(2,4)

    sel_letters = random.choices(letters, k=num_letters)
    sel_numbers = random.choices(numbers, k=num_numbers)
    sel_symbols = random.choices(symbols, k=num_symbols)

    password = sel_letters + sel_numbers + sel_symbols
    random.shuffle(password)
    password = "".join(password)
    
    password_input.delete(0, END)
    password_input.insert(0, password)
    
    pyperclip.copy(password)
    
    

        
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    '''Saves password and corresponding mail and website'''
    email = mail_input.get()
    website = web_input.get()
    password = password_input.get()
    
    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="Missing Information", message="Password/Website is empty. Cannot save")
        return
    
    isok = messagebox.askokcancel(title=website, message=f"these are the details entered\nEmail: {email}\nPassword: {password}\nSave or cancel?")
    
    if isok:
        #append to file
        with open("database.txt", "a") as file:
            file.write(f"{email}|{website}|{password}\n")
            
        web_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg=WHITE)

# Canvas
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
image_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_logo)
canvas.grid(column=1, row=0)

# Website
web_label = Label(text="Website:", bg=WHITE, pady=5)
web_label.grid(column=0, row=1)
web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2, sticky=W, padx=5)

#Email/Username
mail_label = Label(text="Email/Username:", bg=WHITE, pady=5)
mail_label.grid(column=0, row=2)
mail_input = Entry(width=35)
mail_input.insert(0, "email@email.com")
mail_input.grid(column=1, row=2, columnspan=2, sticky=W, padx=5)

#Password
password_label = Label(text="Password:", bg=WHITE, pady=5)
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky=W, padx=5)

#Generate password button
generate_button = Button(text="Generate Password", width=20, command=generate_password)
generate_button.grid(column=2, row=3, sticky=W)

#Add Button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, pady=5, sticky=W)

window.mainloop()