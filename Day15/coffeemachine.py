from coffeemachine_data import MENU

# Remaining resources in coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def printReport():
    ''' print the report of resources left and money collected'''
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    
def checkResources(coffee):
    '''Check if there are enough resources to make the coffee'''
    ingredients = MENU[coffee]["ingredients"]
    enoughResources = True
    
    for key in ingredients:
        if resources[key] < ingredients[key]:
            print(f"Sorry there is not enough of {key}")
            enoughResources = False
            
    return enoughResources

def insertCoins():
    '''Process the coins inserted'''
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    
    dollarSum = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return dollarSum

def transactCoffee(coffee, payment):
    '''Check if the transaction is successful'''
    cost = MENU[coffee]["cost"]
    if payment >= cost:
        change = payment - cost
        resources["money"] += cost
        print(f"Here is ${round(change, 2)} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def makeCoffee(coffee):
    '''Make the coffee'''
    ingredients = MENU[coffee]["ingredients"]
    for key in ingredients:
        resources[key] -= ingredients[key]
    print(f"Here is your {coffee}. Enjoy!")

    
def processCoffee(coffee):
    ''' Process the coffee command'''
    if checkResources(coffee):
        payment = insertCoins()
        if transactCoffee(coffee, payment):
           makeCoffee(coffee)

def refillResources():
    '''Refill the resources in the coffee machine'''
    water = int( input("How much water would you like to refill? ml: "))
    resources["water"] += water
    milk = int( input("How much milk would you like to refill? ml: "))
    resources["milk"] += milk
    coffee = int( input("How much coffee would you like to refill? g: "))
    resources["coffee"] += coffee
    print("Resources refilled")
            

def checkCommand(command):
    ''' Check which command was sent and if its valid'''
    if command == "off":
        return command
    elif command == "report":
        printReport()
    elif command == "refill":
        refillResources()
    elif command in MENU:
        processCoffee(command)
    else:
        print("Invalid command")
        True


def startMachine():
    '''Start the coffee machine'''
    command = ""
    print("Welcome to the coffee machine")
    
    while command != "off":
        command = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
        
        checkCommand(command)
        

startMachine()
