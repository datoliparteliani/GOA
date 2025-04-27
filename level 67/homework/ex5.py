class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        if amount < 0:
            return "Cant deposit negative amount"
        self.balance += amount
        return f"You deposited {amount}, Your balance is {self.balance}"
    def withdraw(self, amount):
        if amount > self.balance:
            return "Balance is not enough"
        elif amount < 0:
            return "Cant withdraw negative amount"
        self.balance -= amount
        return f"You withdrew {amount}, Your balance is {self.balance}"

b1 = BankAccount(800)
print(b1.deposit(200))
print(b1.withdraw(500))