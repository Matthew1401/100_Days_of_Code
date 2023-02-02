import random

names = ['Ales', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# Dictionary comprehension with a list
students_score = {student: random.randint(1, 100) for student in names}
print(students_score)

# Dictionary comprehension with another dictionary
passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
print(passed_students)
