from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
    
    
# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    ''' find password in datafile'''
    website = web_input.get()
    
    # Empty input, return
    if len(website) == 0:
        messagebox.showinfo(title="Missing Information", message="No website to search for.")
        return
    
    data = read_file()
    
    try:
         result = data[website]
         print(result)
    except KeyError:
         messagebox.showinfo(title="No Password Found", message="No data found for website")
    else:
         messagebox.showinfo(title=f"{website}", message=f"Email: {result['email']}\nPassword:{result['password']}")

        
# ---------------------------- SAVE PASSWORD ------------------------------- #
def read_file(data=None):
    ''' reads file, creates new one if file does not exist'''
    result = {}
    try:        
        with open("database.json", "r") as file:
            result = json.load(file)
    except FileNotFoundError:
            write_file()
    except json.JSONDecodeError:
            None
    finally:
            if data:
                result.update(data)
            
    return result

def write_file(data = None):
     '''updates file with new content'''
     with open("database.json", "w") as file:
            if data:
                json.dump(data, file, indent=2)
                web_input.delete(0, END)
                password_input.delete(0, END)

def save_password():
    '''Saves password and corresponding mail and website'''
    email = mail_input.get()
    website = web_input.get()
    password = password_input.get()
    
    new_data = {website: {
        "email": email,
        "password": password
    }}
    
    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="Missing Information", message="Password/Website is empty. Cannot save")
        return
    else:
        data = read_file(new_data)
        write_file(data)

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
web_input = Entry(width=21)
web_input.grid(column=1, row=1, sticky=W, padx=5)

#Search button
search_button = Button(text="Search", width=20, command=search_website)
search_button.grid(column=2, row=1, sticky=W)

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