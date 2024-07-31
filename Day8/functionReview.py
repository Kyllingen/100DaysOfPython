#Write a function called greet
#Write 3 print statements inside the function.
#Call the greet function and run code.

def greet():
    print("Hello")
    print("How are you?")
    print("Goodbye")
    
greet()

#function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")
    print(f"Goodbye {name}")
    
greet_with_name("Carl")

#function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    
greet_with("Carl", "London")
greet_with(location="London", name="Carl") # alternate way