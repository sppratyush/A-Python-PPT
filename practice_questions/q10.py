students = []

n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("Name: ")
    roll = input("Roll: ")
    marks = int(input("Marks: "))

    students.append({"name": name, "roll": roll, "marks": marks})

print("\nPassed Students:")
for s in students:
    if s["marks"] >= 40:
        print(s)