class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        elif amount > self.balance:
            print("Insufficient balance for the withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Account balance: ${self.balance}")

account = BankAccount(account_number="12345678", owner="John Doe", balance=1000)

account.display_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(1500) 
account.display_balance()
