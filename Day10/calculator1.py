
import calculator_art

# Math operators
def add(a, b):
    """Add a and b."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply a by b."""
    return a * b

def divide(a, b):
    """Divide a by b. If b is zero, return an error message."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

math_operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

logo = calculator_art.logo


# Calculations
def calculator():
    calculate_next = True
    result = None
    
    while calculate_next:
        
        if result == None:
            num1 = float(input("Enter the first number: "))

            for operator in math_operators:
                print(operator)
            
        else:
            num1 = result
            
        operator = input("Pick the operator: \n")
        num2 = float(input("Enter the next number: "))

        #Calculation
        math_function = math_operators[operator]
        result = math_function(num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
        
        continue_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, 'q' to quit: ").lower()
        
        if continue_calculation != "y":
            calculate_next = False
            calculator() 
        elif continue_calculation == "q":
            calculate_next = False
            print("Goodbye!")

#starting point
print(logo)
calculator()