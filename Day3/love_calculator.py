print("The Love Calculator is calculating your score...")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# check for the number of times the letters in TRUE appears in the name1 and name2
count1 = name1.lower().count('t') + name1.lower().count('r') + name1.lower().count('u') + name1.lower().count('e')
count2 = name2.lower().count('t') + name2.lower().count('r') + name2.lower().count('u') + name2.lower().count('e')
count1 += count2
#check for number of times the letters LOVE appears in the name1 and name2
count3 = name1.lower().count('l') + name1.lower().count('o') + name1.lower().count('v') + name1.lower().count('e')
count4 = name2.lower().count('l') + name2.lower().count('o') + name2.lower().count('v') + name2.lower().count('e')
count3 += count4             

total_count = int(str(count1) + str(count3))

if total_count < 10 or total_count > 90:
    print(f"Your score is {total_count}, you go together like coke and mentos.")
elif total_count >= 40 and total_count <= 50:
    print(f"Your score is {total_count}, you are alright together.")
else:
    print(f"Your score is {total_count}.")