#examples
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
import random


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {name:random.randint(1,100) for name in names}
print(students_score)

passed_students = {name:score for (name,score) in students_score.items() if score >= 60}
print(passed_students)