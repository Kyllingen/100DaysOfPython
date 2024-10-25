

#open letter
base_letter = "" 
with open("./Input/Letters/starting_letters.txt") as letter:
    base_letter = letter.read()
    
#open file for names

with open("./Input/Names/invited_names.txt") as names:
    for name in names:
        new_letter = str.replace(base_letter, '[name]', name.strip('\n'))
        
        with open('./Output/ReadyTosend/invitation_' + name.strip('\n') + '.txt', 'w') as updated_letter:
            updated_letter.write(new_letter)
            print(updated_letter)