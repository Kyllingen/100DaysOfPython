alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Enter your message:\n").lower()
shift = int(input("Enter the shift number:\n"))

def encrypt(plain_text, shift):
    encrypted_text=""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = ((position + shift) % (len(alphabet)))
        encrypted_text += alphabet[new_position]
    print(f"The encoded text is {encrypted_text}")

#TODO1 - Create a function called 'decrypt' that takes the 
# 'text' and 'shift' as inputs.
#TODO2 - Inside the 'decrypt' function, shift each letter of
#the text backwards in the alphabet by the shift amount and print
#the decrypted text.

def decrypt(cipher_text, shift):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = ((position - shift) % (len(alphabet)))
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")

#TODO3 - Check if the user wanted to encrypt or decrypt the message
# by checking the 'direction' variable. Then call the correct 
#function based on that 'direction' variable. You should be able
#to test the code to encrypt *and* decrypt a message.
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Invalid input. Please try again.")