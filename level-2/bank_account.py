class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: ${self.balance:.2f}")
        else:
            print(f"Invalid amount. please enter a positive number.")

        
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal successful. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:    
            print("Invalid amount. Please enter a positive number.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

def main():
    print("Welcome to the Bank Account Simulation!")
    account_holder = input("Enter the account holder's name: ")
    initial_balance = float(input("Enter the initial balance: "))

    account = BankAccount(account_holder, initial_balance)

    while True:
        print("""
What would you like to do?
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
            
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
            

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            print("Bye! —hazellenuts")
            break
        else:
            print("Invalid choice, Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()