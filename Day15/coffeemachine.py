from coffeemachine_data import MENU

# Remaining resources in coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def print_report():
    ''' print the report of resources left and money collected'''
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    
def check_resources(coffee):
    '''Check if there are enough resources to make the coffee'''
    ingredients = MENU[coffee]["ingredients"]
    enough_resources = True
    
    for key in ingredients:
        if resources[key] < ingredients[key]:
            print(f"Sorry there is not enough of {key}")
            enough_resources = False
            
    return enough_resources

def insert_coins():
    '''Process the coins inserted'''
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    
    dollar_sum = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return dollar_sum

def transact_coffee(coffee, payment):
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

def make_coffee(coffee):
    '''Make the coffee'''
    ingredients = MENU[coffee]["ingredients"]
    for key in ingredients:
        resources[key] -= ingredients[key]
    print(f"Here is your {coffee}. Enjoy!")

    
def process_coffee(coffee):
    ''' Process the coffee command'''
    if check_resources(coffee):
        payment = insert_coins()
        if transact_coffee(coffee, payment):
           make_coffee(coffee)

def refill_resources():
    '''Refill the resources in the coffee machine'''
    water = int( input("How much water would you like to refill? ml: "))
    resources["water"] += water
    milk = int( input("How much milk would you like to refill? ml: "))
    resources["milk"] += milk
    coffee = int( input("How much coffee would you like to refill? g: "))
    resources["coffee"] += coffee
    print("Resources refilled")
            

def check_command(command):
    ''' Check which command was sent and if its valid'''
    if command == "off":
        return command
    elif command == "report":
        print_report()
    elif command == "refill":
        refill_resources()
    elif command in MENU:
        process_coffee(command)
    else:
        print("Invalid command")
        True


def start_machine():
    '''Start the coffee machine'''
    command = ""
    print("Welcome to the coffee machine")
    
    while command != "off":
        command = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
        
        check_command(command)
        

start_machine()
