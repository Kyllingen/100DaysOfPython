alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Enter your message:\n").lower()
shift = int(input("Enter the shift number:\n"))

#TODO1 - combine encrypt and decrypt into a single function called
# caesar()

def caesar(direction, text, shift):
    outputText = ""
    
    if direction == "decode":
        shift *= -1
        
    for letter in text:
        position = alphabet.index(letter)
        newPosition = ((position + shift) % (len(alphabet)))
        outputText += alphabet[newPosition]
        
    print(f"The {direction}d text is {outputText}")

caesar(direction, text, shift)