# List based transaction system
balance = 0
transaction = []
password = 'pratyush123'

def ValidatePassword(p):
    return p == password

def TakeNewPass():
    return input("Enter your new password : ")

def TakePass():
    return input("Enter your password : ")

def TakeDeposite():
    global balance
    amt = int(input("Enter Deposit Amount : "))
    balance += amt
    transaction.append("Deposit : " + str(amt))
    print("Amount Credited To Your Bank Account")

def TakeWithdraw():
    global balance
    amt = int(input("Enter Withdraw Amount : "))
    if balance < amt:
        print("Not enough balance\nPlease deposit first")
    else:
        balance -= amt
        transaction.append("Withdraw : " + str(amt))
        print("Amount Debited From Your Account")

def PrintTransaction():
    print("Transaction History")
    if not transaction:
        print("No Transaction History")
    else:
        for i in transaction:
            print(i)

inputPass = TakePass()
while ValidatePassword(inputPass):
        print("Welcome, You can do the transactions")
        print("\n0. Reset Password")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit\n")

        choice = int(input("Enter your Choice : "))

        if choice == 0:
            password = TakeNewPass()
            continue
        elif choice == 1:
            TakeDeposite()
        elif choice == 2:
            TakeWithdraw()
        elif choice == 3:
            print("Available Balance :", balance)
        elif choice == 4:
            PrintTransaction()
        elif choice == 5:
            print("Thanks for using the system")
            break
        else:
            print("Invalid Input Try Again")
if(ValidatePassword(inputPass)==False):
    print("Wrong password")
