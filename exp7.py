print("Mohammed Ali, 251A007")

students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    attendance = int(input("Enter attendance: "))
    students[name] = {"Marks": marks, "Attendance": attendance}

for name, details in students.items():
    print(name, "->", details)
