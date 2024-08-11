student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
# use for loop to calculate the highest score. 
# do not use min/max functions, only loops
highest_score = 0

for n in student_scores:
    if n > highest_score:
        highest_score = n
        
print(f"The highest score in the class is: {highest_score}")