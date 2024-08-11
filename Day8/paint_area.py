import math
def paint_calc(height, width, cover):
    cans = math.ceil((height * width) / cover)
    print(f"You'll need {cans} cans of paint.")

# how many cans needed based on area
test_h = int(input("Enter height of wall: "))
test_w = int(input("Enter width of wall: "))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)