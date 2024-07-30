import random
from hangman_art import stages, hangman_logo
from hangman_wordlist import word_list

import hangman_wordlist

chosen_word = word_list[random.randint(0, len(word_list)-1)]

user_lives = len(stages) - 1
display = []
guessed_letters = []

print(hangman_logo)

for letter in chosen_word:
    display.append("_")
    
print(f"{' '.join(display)}")

while display.count("_") > 0:
    guess = input("Guess a letter: ").lower()
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        continue
    elif guess not in chosen_word:
      
        print(f"{guess} is not in the word. You lose a life.")
        user_lives -= 1
        if user_lives < 0:
            print("You lose!")
            break

    guessed_letters.append(guess)
    print(f"{' '.join(display)}")
    
    print(f"Guessed letters: {','.join(guessed_letters)}\n")
    
    print(stages[user_lives])
    
if user_lives >= 0:
    print("You win!")