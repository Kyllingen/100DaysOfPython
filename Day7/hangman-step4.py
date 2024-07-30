import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel", "dolphin", 
             "elephant", "flamingo", "giraffe", "hippo", 
             "iguana", "jaguar", "kangaroo", "llama", "monkey", 
             "narwhal", "octopus", "penguin", "quokka", "rhino", 
             "squirrel", "tiger", "unicorn", "vulture", "walrus", 
             "xerus", "yak", "zebra"]

chosen_word = word_list[random.randint(0, len(word_list)-1)]

user_lives = len(stages) - 1
display = []

for letter in chosen_word:
    display.append("_")
    
print(f"{' '.join(display)}")

while display.count("_") > 0:
    guess = input("Guess a letter: ").lower()
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

#TODO-1: - If guess is not a letter in the chosen_word, then
# reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and
# it should print "You lose."
    if guess not in chosen_word:
        user_lives -= 1
        if user_lives < 0:
            print("You lose!")
            break

    print(f"{' '.join(display)}")
    
#TODO-2: - Print the ASCII art from 'stages' that corresponds
# to the current number of 'lives' the user has remaining.
    print(stages[user_lives])
    
if user_lives >= 0:
    print("You win!")