#Random heads or tails
import random

result = random.randint(0, 1)
print(result)
if result == 0:
    print("Heads")
else:
    print("Tails")