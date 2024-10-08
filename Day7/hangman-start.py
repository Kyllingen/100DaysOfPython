import random

word_list = ["aardvark", "baboon", "camel", "dolphin", 
             "elephant", "flamingo", "giraffe", "hippo", 
             "iguana", "jaguar", "kangaroo", "llama", "monkey", 
             "narwhal", "octopus", "penguin", "quokka", "rhino", 
             "squirrel", "tiger", "unicorn", "vulture", "walrus", 
             "xerus", "yak", "zebra"]

#TODO-1: - Randomly choose a word from the word_list and assign
#it to a variable called chosen_word.
chosen_word = word_list[random.randint(0, len(word_list)-1)]

#TODO-2: - Ask the user to guess a letter and assign their 
# answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3: - Check if the letter the user guessed (guess) is one 
# of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
