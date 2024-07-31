import math
def paintCalc(height, width, cover):
    cans = math.ceil((height * width) / cover)
    print(f"You'll need {cans} cans of paint.")

# how many cans needed based on area
testH = int(input("Enter height of wall: "))
testW = int(input("Enter width of wall: "))
coverage = 5
paintCalc(height = testH, width = testW, cover = coverage)