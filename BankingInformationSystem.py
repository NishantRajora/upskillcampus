import os
import json

class User:
    def __init__(self, username, password, balance=0.0):
        self.username = username
        self.password = password
        self.balance = balance

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'balance': self.balance
        }

    @staticmethod
    def from_dict(data):
        return User(data['username'], data['password'], data['balance'])

class BankingInformationSystem:
    def __init__(self, data_file='userdata.txt'):
        self.users = {}
        self.data_file = data_file
        self.load_users()

    def load_users(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for username, user_data in data.items():
                        self.users[username] = User.from_dict(user_data)
        except Exception as e:
            print("Error loading users:", e)

    def save_users(self):
        try:
            with open(self.data_file, 'w') as f:
                json.dump({u: user.to_dict() for u, user in self.users.items()}, f)
        except Exception as e:
            print("Error saving users:", e)

    def register(self):
        username = input("Enter a username: ")
        if username in self.users:
            print("Username already exists.")
            return
        password = input("Enter a password: ")
        self.users[username] = User(username, password)
        self.save_users()
        print("User registered successfully.")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = self.users.get(username)
        if user and user.password == password:
            print("Login successful.")
            self.user_menu(user)
        else:
            print("Invalid credentials.")

    def user_menu(self, user):
        while True:
            print("\n--- Account Menu ---")
            print("1. View Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Logout")
            option = input("Choose an option: ")
            if option == '1':
                print(f"Current Balance: ₹{user.balance:.2f}")
            elif option == '2':
                try:
                    amount = float(input("Enter amount to deposit: ₹"))
                    user.balance += amount
                    self.save_users()
                    print(f"Deposited ₹{amount}. New balance: ₹{user.balance:.2f}")
                except ValueError:
                    print("Invalid amount.")
            elif option == '3':
                try:
                    amount = float(input("Enter amount to withdraw: ₹"))
                    if amount > user.balance:
                        print("Insufficient balance.")
                    else:
                        user.balance -= amount
                        self.save_users()
                        print(f"Withdrew ₹{amount}. Remaining balance: ₹{user.balance:.2f}")
                except ValueError:
                    print("Invalid amount.")
            elif option == '4':
                print("Logged out successfully.")
                break
            else:
                print("Invalid option.")

    def start(self):
        print("Welcome to the Banking Information System")
        while True:
            print("\n1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.register()
            elif choice == '2':
                self.login()
            elif choice == '3':
                print("Thank you for using the system!")
                self.save_users()
                break
            else:
                print("Invalid option.")

if __name__ == "__main__":
    BankingInformationSystem().start()
