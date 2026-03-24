employees = {}

while True:
    print("\n1.Add 2.Remove 3.Display 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        name = input("Employee name: ")
        employees[name] = "Present"

    elif ch == "2":
        name = input("Remove name: ")
        employees.pop(name, None)

    elif ch == "3":
        print(employees)

    elif ch == "4":
        break