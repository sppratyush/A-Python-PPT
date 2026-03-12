"""3.Banking System with Transactions 
Simulate real-time transactions between bank accounts. 
Handle errors like overdraft, transaction timeout, incorrect account numbers."""
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target account must be a BankAccount instance.")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        self.withdraw(amount)
        target_account.deposit(amount)
# Example usage
if __name__ == "__main__":
    account1 = BankAccount("123456", 1000)
    account2 = BankAccount("654321", 500)
    try:
        account1.transfer(account2, 200)
        print("Account 1 balance:", account1.balance)  # Output: 800
        print("Account 2 balance:", account2.balance)  # Output: 700
        account1.transfer(account2, 900)  # This will raise an exception
    except (ValueError, TypeError) as e:
        print("Error:", e)
        