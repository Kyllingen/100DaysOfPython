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
result_list = [["It's a draw", "You lose", "You win"], 
             ["You win", "It's a draw", "You lose"], 
             ["You lose", "You win", "It's a draw"]]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())

# Logic
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
    
computer_choice = random.randint(0, 2)
result = result_list[user_choice][computer_choice]

# Game output
print(list[user_choice] + "\n")
print("Computer chose:\n")
print(list[computer_choice] + "\n")
print(result)
