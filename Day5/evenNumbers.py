target = int(input("Enter target number to add up to:"))

evenSum = 0
for i in range(0, target + 1, 2):
    evenSum += i
    
print(evenSum)