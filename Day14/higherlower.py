
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

def get_comparison_accounts(compare_accounts):
    '''Get two accounts to compare followers against'''
    #First time, populate both
    if len(compare_accounts) == 0:
        compare_accounts.append(random.choice(higherlower_data.data))
        compare_accounts.append(random.choice(higherlower_data.data))
    else:
        compare_accounts[0] = compare_accounts[1]
        compare_accounts[1] = random.choice(higherlower_data.data)
        
    return compare_accounts

def print_compare_followers(compare_accounts):
    '''Print the two accounts to compare followers against'''
    print(f"Compare A: {compare_accounts[0]['name']}, a {compare_accounts[0]['description']}, from {compare_accounts[0].get('country')}")
    
    print(higherlower_art.vs)
    
    print(f"Against B: {compare_accounts[1]['name']}, a {compare_accounts[1]['description']}, from {compare_accounts[1].get('country')}")
    print("Who has more followers? Type 'A' or 'B':")
    
def check_answer(compare_accounts, answer):
    '''Check if the answer is correct'''
    if compare_accounts[0]['follower_count'] >= compare_accounts[1]['follower_count']:
        return answer == 'A'
    elif compare_accounts[0]['follower_count'] <= compare_accounts[1]['follower_count']:
        return answer == 'B'
    else:
        return False

def clear_screen():
    '''Clear the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')
    
def play_game():
    ''' play the game and keep playing until user gets answer wrong'''
    
    still_playing = True
    compare_accounts = []
    score = 0
    correct_answer = None
    
    while still_playing:
        #clear screen
        clear_screen()
        print(higherlower_art.logo + "\n")
        if correct_answer == True:
            score += 1
            print(f"You're right! Current score: {score}.")
        elif correct_answer == False:
            print(f"Sorry, that's wrong. Final score: {score}.")
            still_playing = False
            break
        
        compare_accounts = get_comparison_accounts(compare_accounts)
        print_compare_followers(compare_accounts)
        
        answer = input().upper()
        correct_answer = check_answer(compare_accounts, answer)

play_game()