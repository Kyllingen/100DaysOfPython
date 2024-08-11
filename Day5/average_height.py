student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    
# go throug student list and add all the heights
# dont use len or sum functions, use a for loop
total_height = 0
number_of_students = 0
for n in student_heights:
    total_height += n
    number_of_students += 1
    
average_height = round(total_height / number_of_students)
print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")