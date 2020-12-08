student_heights = input("Input a list of student heights\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

number_students = 0
for student in student_heights:
    number_students += 1

average_height = round(total_height / number_students)
print(f'total height = {total_height}')
print(f'number of students = {number_students}')
print(f'average height = {average_height}')
