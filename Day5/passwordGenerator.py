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
numLetters = int(input("How many letters would you like in your password?"))
numSymbols = int(input("How many symbols would you like?"))
numNumbers = int(input("How many numbers would you like?"))

totalLength = numLetters + numSymbols + numNumbers
list = ["letters", "symbols", "numbers"]

password = ""

#this could have been simplifed by using random.shuffle(), but keeping this as a solution
for i in range(0, totalLength):
    
    randomChoice = random.randint(0, len(list)-1)
    
    if list[randomChoice] == "letters":
        password += random.choice(letters)
        numLetters -= 1
    elif list[randomChoice] == "symbols":
        password += random.choice(symbols)
        numSymbols -= 1
    else:
        password += random.choice(numbers)
        numNumbers -= 1
    
    if numLetters == 0:
        list.remove("letters")
        numLetters = -1
    if numSymbols == 0:
        list.remove("symbols")
        numSymbols = -1
    if numNumbers == 0:
        list.remove("numbers")
        numNumbers = -1
        
    

print(f"Your password is: {password}")  




