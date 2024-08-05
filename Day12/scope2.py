#Modify global scope

enemies = "Skeleton"

# the below code will use two different variables for enemies.
def increaseEnemies():
    enemies = "Zombie"
    print(f"Enemies inside function: {enemies}")  
    
# the below code will use the global variable for enemies.
def increaseEnemiesGlobal():
    global enemies
    enemies = "Zombie"
    print(f"Enemies inside function: {enemies}")  
    
# a better option is to pass the variable as a parameter
def increaseEnemiesParams(enemies):
    enemies = "Dragon"
    print(f"Enemies inside function: {enemies}")
    return enemies

increaseEnemies()
print(f"Enemies outside function: {enemies}")

increaseEnemiesGlobal()
print(f"Enemies outside function: {enemies}")

enemies = increaseEnemiesParams(enemies)
print(f"Enemies outside function: {enemies}")