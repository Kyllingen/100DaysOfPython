target = int(input("Enter target number to add up to:"))

even_sum = 0
for i in range(0, target + 1, 2):
    even_sum += i
    
print(even_sum)