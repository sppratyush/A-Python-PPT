#Securely store, add, edit, and retrieve user passwords using encryption.
import hashlib
import os
class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def hash_password(self, password):
        # Hash the password using SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

    def add_password(self, username, password):
        hashed_password = self.hash_password(password)
        self.passwords[username] = hashed_password
        print(f"Password for {username} added successfully.")

    def edit_password(self, username, new_password):
        if username in self.passwords:
            hashed_password = self.hash_password(new_password)
            self.passwords[username] = hashed_password
            print(f"Password for {username} updated successfully.")
        else:
            print(f"Username {username} not found.")

    def retrieve_password(self, username):
        if username in self.passwords:
            print(f"Password for {username}: {self.passwords[username]}")
        else:
            print(f"Username {username} not found.")
if __name__ == "__main__":
    manager = PasswordManager()
    while True:
        print("\n1. Add Password")
        print("\n2. Edit Password")
        print("\n3. Retrieve Password")
        print("\n4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            manager.add_password(username, password)
        elif choice == 2:
            username = input("Enter username: ")
            new_password = input("Enter new password: ")
            manager.edit_password(username, new_password)
        elif choice == 3:
            username = input("Enter username: ")
            manager.retrieve_password(username)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
            