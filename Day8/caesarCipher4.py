alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z"]

restart = True
#TODO 1 - import art
import caesar_cipher_art as caesar_cipher_art
print(caesar_cipher_art.caesar_cipher_logo)

#TODO 4 - Can you figure out a way to ask the user if they want to restart cipher program?
# Create a new function to restart everything if they type 'yes

def new_input():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Enter your message:\n").lower()
    shift = int(input("Enter the shift number:\n"))
    caesar(direction, text, shift)


def caesar(direction, text, shift):
    output_text = ""
    
    if direction == "decode":
        shift *= -1
        
    for letter in text:
        #TODO3 - What happens if user enters a number/special character?
        # Can you make the code handle that by keeping symbol or number
        if letter not in alphabet:
            output_text += letter
            continue
        
        position = alphabet.index(letter)
        new_position = ((position + shift) % (len(alphabet)))
        output_text += alphabet[new_position]
        
    print(f"The {direction}d text is: {output_text}\n\n")
    
#TODO2 - What if the user enters a shift that is greater than the number of letters in the alphabet?


while restart:
    new_input()
    
    print("Would you like to restart the cipher program?")
    try_again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if try_again != "yes":
        print("Goodbye!")
        break