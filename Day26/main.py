import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

students_scores = {name:random.randint(1, 100) for name in names}

print(students_scores)

passed_students = {name:students_scores[name] for name in students_scores if students_scores[name] > 49}

print(passed_students)