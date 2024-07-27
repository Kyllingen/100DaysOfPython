print("Welcome to the tip calculator")
print("What was the total bill? $") 
bill = input()
print("How much tip would you like to give? 10, 12, or 15?")
tip = input()
print("How many people to split the bill?")
people = input()

total_bill = (float(bill) + float(bill) * float(tip) / 100) 
bill_per_person = total_bill / float(people)
final_bill = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_bill}")
