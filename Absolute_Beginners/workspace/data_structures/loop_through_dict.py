student_count = {
    'course1': 789,
    'course2': 69674,
    'course3': 122,
}
# Loop through items in dictionary
for k, v in student_count.items():
    print(k,':', v)

# Count the total number of students
total_student = 0
for k, v in student_count.items():
    total_student += v

print('Total Student', total_student)

# get all keys from the dictionary
courses = student_count.keys()
print(courses)
