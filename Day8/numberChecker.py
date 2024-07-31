import math
def primeChecker(number):
    isPrime = True
    endRange = math.ceil(math.sqrt(number)) + 1
    for i in range(2, endRange):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Enter a number: "))
primeChecker(number=n)