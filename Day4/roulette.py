import random
names = []

print("Enter the names of the people playing the game, comma separated")
names = input().split(", ")

random_index = random.randint(0, len(names) - 1)
print(f"{names[random_index]} is going to buy the meal today!")
