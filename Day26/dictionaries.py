#examples
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
import random
import pandas


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {name:random.randint(1,100) for name in names}
print(students_score)

passed_students = {name:score for (name,score) in students_score.items() if score >= 60}
print(passed_students)

# loop through dataframes by rows
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_frame = pandas.DataFrame(student_dict)
print(student_frame)

for (index, row) in student_frame.iterrows():
    print(row)
    print(row.student)
