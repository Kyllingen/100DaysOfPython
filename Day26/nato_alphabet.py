import pandas

#Read in NATO csv
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary in format:
# {"A": "Alpha", "B": "Bravo".... }
nato_dict = {row.letter:row.code for (index,row) in nato_alphabet.iterrows()}

#Create a list of codes based on input text
word = input("Enter a word: ").upper()
phonetics = [nato_dict[letter] for letter in word if letter.isalpha()]
print(phonetics)