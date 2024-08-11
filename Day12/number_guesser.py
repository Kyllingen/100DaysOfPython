"Welcome to the Number Guessing Game"
"Im thinking of a number between 1 and 100"
"Choose a difficulty. Type 'easy' or 'hard':"

#Hard gives 5 attempts to guess. Easy gives 10 attempts
"Too High"
"Guess Again"
"You have 4 attempts remaining to guess the number"
"Youve run out of guesses, you lose"

"You got it! The answer was xx"

import random
import number_guesser_art as number_guesser_art

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5

def set_number_to_guess():
    '''Set the number to guess'''
    print("Im thinking of a number between 1 and 100")
    return random.randint(1, 100)

def set_difficulty():
    '''Set the difficulty level - number of guesses'''
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    if difficulty == 'hard':
        return HARD_DIFFICULTY
    else:
        return EASY_DIFFICULTY

def play_game(number_to_guess, guesses_left):
    ''' Guess number whilst there are guesses left'''
    while guesses_left > 0:
        print(f"Guess the number. You have {guesses_left} attempts remaining")
        guess = int(input("Make a guess: "))
        
        if guess > number_to_guess:
            print("Too High")
        elif guess < number_to_guess:
            print("Too Low")
        else:
            print(f"You got it! The answer was {number_to_guess}")
            return #Exit the function. We have guessed the number
        
        guesses_left -= 1
    
    #If we get here, we have run out of guesses
    print("Youve run out of guesses, you lose")

logo = number_guesser_art.logo

print(logo)
print("Welcome to the Number Guessing Game")
number_to_guess = set_number_to_guess()
guesses_left = set_difficulty()
play_game(number_to_guess, guesses_left)