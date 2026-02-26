n = int(input("Enter the number of students : "))
d = {}
print("Enter ",n," students names & their respective marks :")
for i in range(n):
    name = input("Name : ")
    marks = input("Marks : ")
    d[name] = int(marks)
max = 0
for i in d:
    if d[i] > max:
        max = d[i]
        name = i
print("The maximum marks are : ",max," and it is scored by ", name)