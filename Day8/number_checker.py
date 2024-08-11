import math
def prime_checker(number):
    is_prime = True
    end_range = math.ceil(math.sqrt(number)) + 1
    for i in range(2, end_range):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Enter a number: "))
prime_checker(number=n)