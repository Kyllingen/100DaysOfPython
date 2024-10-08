alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Enter your message:\n").lower()
shift = int(input("Enter the shift number:\n"))

#TODO1-1: Create a function called 'encrypt' that takes the 
# 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of 
# the 'text' forwards in the alphabet by the shift amount and
# print the encrypted text.

def encrypt(text, shift):
    encrypted_text=""
    for letter in text:
        position = alphabet.index(letter)
        new_position = ((position + shift) % (len(alphabet)))
        encrypted_text += alphabet[new_position]
    print(f"The encoded text is {encrypted_text}")

#TODO-3: Call the 'encrypt' function and pass in the user inputs.
# You should be able to test the code and encrypt a message.
encrypt(text, shift)