#Tracker system
entered_std = set()
rejected_std = set()

while True:
        print("\n1.Entry Students")
        print("\n2.Display students")
        print("\n3.Exit")
        choise = int(input("Enter your Choice :"))
        if(choise == 1):
            n = int(input("Enter the number of person :"))
            for i in range(n):
                name = input("Enter your name : ")
                if name in entered_std:
                    print(name, "Already Entered. Entry Rejected")
                    rejected_std.add(name)
                else:
                    entered_std.add(name)
        elif(choise==2):
             for i in entered_std:
                  print(i,)
