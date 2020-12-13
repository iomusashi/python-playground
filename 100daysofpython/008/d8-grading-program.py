student_scores = {
    'Harry': 81,
    'Ron': 78,
    'Hermoine': 99,
    'Draco': 74,
    'Neville': 62,
}

for student in student_scores:
    score = student_scores[student]
    if score > 90 and score <= 100:
        student_scores[student] = 'Outstanding'
    elif score > 80 and score <= 90:
        student_scores[student] = 'Exceeds Expectations'
    elif score > 70 and score <= 80:
        student_scores[student] = 'Acceptable'
    else:
        student_scores[student] = 'Fail'

print(student_scores)
