alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Enter your message:\n").lower()
shift = int(input("Enter the shift number:\n"))

#TODO1 - combine encrypt and decrypt into a single function called
# caesar()

def caesar(direction, text, shift):
    output_text = ""
    
    if direction == "decode":
        shift *= -1
        
    for letter in text:
        position = alphabet.index(letter)
        new_position = ((position + shift) % (len(alphabet)))
        output_text += alphabet[new_position]
        
    print(f"The {direction}d text is {output_text}")

caesar(direction, text, shift)