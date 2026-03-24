contacts = {}

while True:
    print("\n1.Add 2.Search 3.Delete 4.List 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif ch == "2":
        name = input("Search name: ")
        print(contacts.get(name, "Not found"))

    elif ch == "3":
        name = input("Delete name: ")
        contacts.pop(name, None)

    elif ch == "4":
        print(contacts)

    elif ch == "5":
        break