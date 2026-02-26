#List based transaction system
balance = 0
transaction = []
password = 'pratyush123'
def ValidatePassword(p):
    if(p==password):
        return True
    return False
while True:
    inputPass = input("Enter your password :")
    if(ValidatePassword(inputPass)):
        print("Welcome, You can do the transactions")
        print("\n0.Reset Password")
        print("\n1.Deposit")
        print("\n2.Withdraw")
        print("\n3.Check Balance")
        print("\n4.Transaction History")
        print("\n5.Exit\n")
        choise = int(input("Enter your Choice :"))
        if(choise==0):
            password = input("Enter a new password :")
            continue

        if(choise == 1):
            amt = int(input("Enter Deposit Amount : "))
            balance += amt 
            transaction.append("Deposit : "+ str(amt))
            print("Amount Credited To Your Bank Account")
        elif(choise==2):
            amt = int(input("Enter Withdraw Amount :"))
            if(balance<amt):
                print("Not enougn balance\nPlease deposit first")
            else:
                balance-=amt 
                transaction.append("Withdraw : "+str(amt))
        elif(choise==3):
            print("Available Balance :",balance)
        elif(choise==4):
            print("Transaction History")
            if(transaction==[]):
                print("No Transaction History")
            else:
                for i in transaction:
                    print(i)
        elif(choise==5):
            print("Thanks for using the system")
            break
        else:
            print("Invalid Input Try Again")
    else:
        print("Wrong password")
    