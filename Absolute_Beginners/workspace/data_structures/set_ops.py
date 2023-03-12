course_a = {'segun', 'hemmy', 'Simon', 'Mark', 'peter', 'Anand', 'Kath'}
course_b = {'simon', 'segun', 'Suresh', 'Peter', 'Grag', 'Kath', 'Sadie'}

# Students who took both courses (intersection)
intersect = course_a & course_b
print(f'Took both  courses: {intersect}')

# Students from both courses combined (union)
union = course_a | course_b
print(f'All students: {union}')

# Creat a set of stundets who took only one course (symmetric_difference)
sym_diff = course_a ^ course_b
print(f'Took one course: {sym_diff}')