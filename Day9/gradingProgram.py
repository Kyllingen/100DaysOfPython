studentScores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

studentGrades = {}

for student in studentScores:
    score = studentScores[student]
    if score >= 91:
        studentGrades[student] = "Outstanding"
    elif score >= 81:
        studentGrades[student] = "Exceeds Expectations"
    elif score >= 71:
        studentGrades[student] = "Acceptable"
    else:
        studentGrades[student] = "Fail"
        
print(studentGrades)
