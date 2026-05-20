# nums = [1, 2, 3]
# new_nums = [n+1 for n in nums]
# print(new_nums)


# new_lst = [n * 2 for n in range(1, 5)]
# print(new_lst)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# new_names = [name.upper() for name in names if len(name) > 5]
# print(new_names)

import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = {name : random.randint(1, 100) for name in names}
passed_students = {name : marks for (name, marks) in student_scores.items() if marks > 60}
print(student_scores)
print(passed_students)