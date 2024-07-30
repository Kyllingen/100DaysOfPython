import random

word_list = ["aardvark", "baboon", "camel", "dolphin", 
             "elephant", "flamingo", "giraffe", "hippo", 
             "iguana", "jaguar", "kangaroo", "llama", "monkey", 
             "narwhal", "octopus", "penguin", "quokka", "rhino", 
             "squirrel", "tiger", "unicorn", "vulture", "walrus", 
             "xerus", "yak", "zebra"]

chosen_word = word_list[random.randint(0, len(word_list)-1)]


display = []
for letter in chosen_word:
    display.append("_")
    
print(display)

#TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the 
# letters in the chosen_word and 'display' has no more blanks 
# ("_"). Then you can tell the user they've won.
while display.count("_") > 0:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    print(display)
    
print("You win!")