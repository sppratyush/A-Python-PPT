students = {}

def add_student(name, marks):
    students[name] = marks

def update_marks(name, new_marks):
    students[name] = new_marks

def average(name):
    return sum(students[name]) / len(students[name])

def topper():
    return max(students, key=lambda x: sum(students[x]))

add_student("Aman", [80, 90, 85])
add_student("Riya", [95, 92, 90])

update_marks("Aman", [88, 89, 90])

print("Average Aman:", average("Aman"))
print("Topper:", topper())