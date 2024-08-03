
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

mathOperators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

logo = calculator_art.logo


# Calculations
def calculator():
    calculateNext = True
    result = None
    
    while calculateNext:
        
        if result == None:
            num1 = float(input("Enter the first number: "))

            for operator in mathOperators:
                print(operator)
            
        else:
            num1 = result
            
        operator = input("Pick the operator: \n")
        num2 = float(input("Enter the next number: "))

        #Calculation
        mathFunction = mathOperators[operator]
        result = mathFunction(num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
        
        continueCalculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, 'q' to quit: ").lower()
        
        if continueCalculation != "y":
            calculateNext = False
            calculator() 
        elif continueCalculation == "q":
            calculateNext = False
            print("Goodbye!")

#starting point
print(logo)
calculator()