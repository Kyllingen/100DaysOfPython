
#print logo for each turn
# Compare A: xxxx
# vs logo
# Against B: yyyy
# Who has more followers? Type 'A' or 'B':

# On top. "Youre right! Current score: 1."
#Move B as A and find new B
#else, "Sorry, that's wrong. Final score: 1. Quit"

import random
import os
import higherlower_art
import higherlower_data

def getComparisonAccounts(compareAccounts):
    '''Get two accounts to compare followers against'''
    #First time, populate both
    if len(compareAccounts) == 0:
        compareAccounts.append(random.choice(higherlower_data.data))
        compareAccounts.append(random.choice(higherlower_data.data))
    else:
        compareAccounts[0] = compareAccounts[1]
        compareAccounts[1] = random.choice(higherlower_data.data)
        
    return compareAccounts

def printCompareFollowers(compareAccounts):
    '''Print the two accounts to compare followers against'''
    print(f"Compare A: {compareAccounts[0]['name']}, a {compareAccounts[0]['description']}, from {compareAccounts[0].get('country')}")
    
    print(higherlower_art.vs)
    
    print(f"Against B: {compareAccounts[1]['name']}, a {compareAccounts[1]['description']}, from {compareAccounts[1].get('country')}")
    print("Who has more followers? Type 'A' or 'B':")
    
def checkAnswer(compareAccounts, answer):
    '''Check if the answer is correct'''
    if compareAccounts[0]['follower_count'] >= compareAccounts[1]['follower_count']:
        return answer == 'A'
    elif compareAccounts[0]['follower_count'] <= compareAccounts[1]['follower_count']:
        return answer == 'B'
    else:
        return False

def clearScreen():
    '''Clear the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')
    
def playGame():
    ''' play the game and keep playing until user gets answer wrong'''
    
    stillPlaying = True
    compareAccounts = []
    score = 0
    correctAnswer = None
    
    while stillPlaying:
        #clear screen
        clearScreen()
        print(higherlower_art.logo + "\n")
        if correctAnswer == True:
            score += 1
            print(f"You're right! Current score: {score}.")
        elif correctAnswer == False:
            print(f"Sorry, that's wrong. Final score: {score}.")
            stillPlaying = False
            break
        
        compareAccounts = getComparisonAccounts(compareAccounts)
        printCompareFollowers(compareAccounts)
        
        answer = input().upper()
        correctAnswer = checkAnswer(compareAccounts, answer)

playGame()