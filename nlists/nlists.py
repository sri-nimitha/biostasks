a=int(input())
input_arr=[[input(),float(input())] for _ in range(0,a)]
input_arr.sort(key=lambda k: (k[1],k[0]))
names_of_students = [i[0] for i in input_arr]
marks_of_students = [i[1] for i in input_arr]
min_value_of_marks=min(marks_of_students)
while marks_of_students[0]==min_value_of_marks:
    marks_of_students.remove(marks_of_students[0])
    names_of_students.remove(names_of_students[0])    
for k in range(0,len(marks_of_students)):
    if marks_of_students[k]==min(marks_of_students):
        print(names_of_students[k])
