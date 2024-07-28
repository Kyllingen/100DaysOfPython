studentHeights = input("Input a list of student heights ").split()
for n in range(0, len(studentHeights)):
    studentHeights[n] = int(studentHeights[n])
    
# go throug student list and add all the heights
# dont use len or sum functions, use a for loop
totalHeight = 0
numberOfStudents = 0
for n in studentHeights:
    totalHeight += n
    numberOfStudents += 1
    
averageHeight = round(totalHeight / numberOfStudents)
print(f"total height = {totalHeight}")
print(f"number of students = {numberOfStudents}")
print(f"average height = {averageHeight}")