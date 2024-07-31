alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z"]

restart = True
#TODO 1 - import art
import caesarCipher_art
print(caesarCipher_art.caesarCipherLogo)

#TODO 4 - Can you figure out a way to ask the user if they want to restart cipher program?
# Create a new function to restart everything if they type 'yes

def newInput():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Enter your message:\n").lower()
    shift = int(input("Enter the shift number:\n"))
    caesar(direction, text, shift)


def caesar(direction, text, shift):
    outputText = ""
    
    if direction == "decode":
        shift *= -1
        
    for letter in text:
        #TODO3 - What happens if user enters a number/special character?
        # Can you make the code handle that by keeping symbol or number
        if letter not in alphabet:
            outputText += letter
            continue
        
        position = alphabet.index(letter)
        newPosition = ((position + shift) % (len(alphabet)))
        outputText += alphabet[newPosition]
        
    print(f"The {direction}d text is: {outputText}\n\n")
    
#TODO2 - What if the user enters a shift that is greater than the number of letters in the alphabet?


while restart:
    newInput()
    
    print("Would you like to restart the cipher program?")
    tryAgain = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if tryAgain != "yes":
        print("Goodbye!")
        break