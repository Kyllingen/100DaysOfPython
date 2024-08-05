# Scope test

enemies = 1

def increaseEnemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increaseEnemies()
print(f"Enemies outside function: {enemies}")

######################
# Global scope
playerHealth = 10
# local scope
def drinkPotion():
    potionStrength = 2
    print(playerHealth)  # Can call this as its in global scope
    print(potionStrength)
    
######################
drinkPotion()
#print(potionStrength)  # cant call this. Name not defined

######################
#No block scope. Variables defined in a block are available outside the block
gamesLevel = 3
if gamesLevel < 5:
    levelDifficulty = "easy"
    
print(levelDifficulty)