import random

# static data for use
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
           'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?"))
num_symbols = int(input("How many symbols would you like?"))
num_numbers = int(input("How many numbers would you like?"))

total_length = num_letters + num_symbols + num_numbers
list = ["letters", "symbols", "numbers"]

password = ""

#this could have been simplifed by using random.shuffle(), but keeping this as a solution
for i in range(0, total_length):
    
    random_choice = random.randint(0, len(list)-1)
    
    if list[random_choice] == "letters":
        password += random.choice(letters)
        num_letters -= 1
    elif list[random_choice] == "symbols":
        password += random.choice(symbols)
        num_symbols -= 1
    else:
        password += random.choice(numbers)
        num_numbers -= 1
    
    if num_letters == 0:
        list.remove("letters")
        num_letters = -1
    if num_symbols == 0:
        list.remove("symbols")
        num_symbols = -1
    if num_numbers == 0:
        list.remove("numbers")
        num_numbers = -1
        
    

print(f"Your password is: {password}")  




