studentScores = input("Input a list of student scores ").split()
for n in range(0, len(studentScores)):
    studentScores[n] = int(studentScores[n])
    
# use for loop to calculate the highest score. 
# do not use min/max functions, only loops
highestScore = 0

for n in studentScores:
    if n > highestScore:
        highestScore = n
        
print(f"The highest score in the class is: {highestScore}")