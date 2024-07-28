import random

#ascii art 
rock = '''
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
            ______)
            _______)
              _______)
---.__________)     
'''

scissors = '''
    _______     
---'   ____)____
            ______)
        __________)
        (____)
---.__(___)
''' 

list = [rock, paper, scissors]
resultList = [["It's a draw", "You lose", "You win"], 
             ["You win", "It's a draw", "You lose"], 
             ["You lose", "You win", "It's a draw"]]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
userChoice = int(input())

# Logic
computerChoice = random.randint(0, 2)
result = resultList[userChoice][computerChoice]

# Game output
print(list[userChoice] + "\n")
print("Computer chose:\n")
print(list[computerChoice] + "\n")
print(result)
