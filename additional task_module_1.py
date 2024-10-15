grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_new = list(students)
students_new.sort()
print(students_new)
# students_new = students_new.sort()
def average_score_students(grades):
    n = []
    for i in grades:
        a = sum(i)/len(i)
        n.append(a)
    return n
average = average_score_students(grades)
resalt = dict(zip(students_new, average))
print(resalt)





