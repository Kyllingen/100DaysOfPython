import random

word_list = ["aardvark", "baboon", "camel", "dolphin", 
             "elephant", "flamingo", "giraffe", "hippo", 
             "iguana", "jaguar", "kangaroo", "llama", "monkey", 
             "narwhal", "octopus", "penguin", "quokka", "rhino", 
             "squirrel", "tiger", "unicorn", "vulture", "walrus", 
             "xerus", "yak", "zebra"]

chosen_word = word_list[random.randint(0, len(word_list)-1)]

#TODO-1: - Create an empty list called display. 
# For each letter in the chosen_word, add a "_" to display.
#So if the chosen_word was "apple", display should be
#  ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
for letter in chosen_word:
    display.append("_")
    
print(display)

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess', then reveal that letter in the display at that position.

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

#TODO-3: - Print | display | to show the current state of the word.
print(display)