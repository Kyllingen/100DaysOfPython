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
import numberGuesser_art

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5

def setNumberToGuess():
    '''Set the number to guess'''
    print("Im thinking of a number between 1 and 100")
    return random.randint(1, 100)

def setDifficulty():
    '''Set the difficulty level - number of guesses'''
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    if difficulty == 'hard':
        return HARD_DIFFICULTY
    else:
        return EASY_DIFFICULTY

def playGame(numberToGuess, guessesLeft):
    ''' Guess number whilst there are guesses left'''
    while guessesLeft > 0:
        print(f"Guess the number. You have {guessesLeft} attempts remaining")
        guess = int(input("Make a guess: "))
        
        if guess > numberToGuess:
            print("Too High")
        elif guess < numberToGuess:
            print("Too Low")
        else:
            print(f"You got it! The answer was {numberToGuess}")
            return #Exit the function. We have guessed the number
        
        guessesLeft -= 1
    
    #If we get here, we have run out of guesses
    print("Youve run out of guesses, you lose")

logo = numberGuesser_art.logo

print(logo)
print("Welcome to the Number Guessing Game")
numberToGuess = setNumberToGuess()
guessesLeft = setDifficulty()
playGame(numberToGuess, guessesLeft)