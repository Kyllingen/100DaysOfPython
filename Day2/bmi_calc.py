print("Plrase enter your weight in kg:")
weight = input()
print("Please enter your height in m:")
height = input()

bmi = float(weight) / float(height) ** 2

print("Your BMI is: " + str(int(bmi)))