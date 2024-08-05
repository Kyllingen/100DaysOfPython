year = int(input("Which year do you want to check? "))

# Bug, not having ">="" in elif statement
if year > 1980 and year < 1994:
    print("You are a millenial")
elif year > 1994:
    print("You are a Gen Z")
    
################
#Adding try / except block to catch errors
try:
    age = int(input("How old are you? "))
except ValueError:
    print("Please enter a valid number")
    
if age > 18:
    print(f"You can drive at {age}")