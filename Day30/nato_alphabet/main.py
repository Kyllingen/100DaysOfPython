import pandas

valid_word = False

#Read in NATO csv
nato_alphabet = pandas.read_csv("../../Day26/nato_phonetic_alphabet.csv")

# Create a dictionary in format:
# {"A": "Alpha", "B": "Bravo".... }
nato_dict = {row.letter:row.code for (index,row) in nato_alphabet.iterrows()}

#Create a list of codes based on input text
while not valid_word:
    word = input("Enter a word: ").upper()
    try:
        phonetics = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only characters in alphabet allowed")
    else:
        valid_word = True
    
print(phonetics)