class User:
    def __init__(self,name):
        self.name = name
        self.balance = 0
    
    def makeDeposit(self,amount):
        self.balance += amount
        return self

    def checkBalance(self, amount):
        if(self.balance < amount):
            print(f"{self.name} only has {self.balance} left")
            return False
        else:
            return True

    def makeWithdrawal(self,amount):
        if(self.checkBalance(amount)):
            self.balance -= amount
        return self

    def displayBalance(self):
        print(f"{self.name} Balance: {self.balance}")

    def transferBalance(self, user, amount):
        if(self.checkBalance(amount)):
            self.balance -= amount
            user.balance += amount
            self.displayBalance()
            user.displayBalance()
        return self

    def __repr__(self):
        return f"Name: {self.name} Balance: {self.balance}"

jim = User("Jim")
jim.makeDeposit(100).makeDeposit(500).makeDeposit(20).displayBalance()

dwight = User("Dwight")
dwight.makeDeposit(10).makeDeposit(1000).makeWithdrawal(500).displayBalance()

pam = User("Pam")
pam.makeDeposit(400).makeWithdrawal(10).makeWithdrawal(50).makeWithdrawal(30).displayBalance()

jim.transferBalance(pam, 30)