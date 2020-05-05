class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.balance = balance
        self.intRate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.checkBalance(amount):
            self.balance -= amount
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def checkBalance(self, amount):
        if(self.balance < amount):
            print(f"You don't have enough money. Balance: {self.balance}")
            return False
        else:
            return True

    def displayAccountInfo(self):
        print(f"Balance: ${self.balance:.2f}")
        return self

    def yieldInterest(self):
        if(self.balance > 0):
            self.balance *= 1+ self.intRate
        return self

    def __repr__(self):
        return f"Balance: {self.balance:.2f} Interest Rate: {self.intRate}"

user1 = BankAccount(.1,100)
user2 = BankAccount(.2,1)

user1.deposit(5).deposit(500).deposit(10).withdraw(300).yieldInterest().displayAccountInfo()

user2.deposit(100).deposit(300).withdraw(100).withdraw(100).withdraw(100).withdraw(200).yieldInterest().displayAccountInfo()