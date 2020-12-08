student_scores = input("Input a list of student scores\n").split()
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])

max_score = 0
for score in student_scores:
    max_score = score if max_score < score else max_score

print(f'The highest score in the class is: {max_score}')
