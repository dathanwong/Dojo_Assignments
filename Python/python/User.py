class User:
    def __init__(self,name):
        self.name = name
        self.balance = 0
    
    def makeDeposit(self,amount):
        self.balance += amount

    def checkBalance(self, amount):
        if(self.balance < amount):
            print(f"{self.name} only has {self.balance} left")
            return False
        else:
            return True

    def makeWithdrawal(self,amount):
        if(self.checkBalance(amount)):
            self.balance -= amount

    def displayBalance(self):
        print(f"Balance: {self.balance}")

    def transferBalance(self, user, amount):
        if(self.checkBalance(amount)):
            self.balance -= amount
            user.balance += amount
            self.displayBalance()
            user.displayBalance()

    def __repr__(self):
        return f"Name: {self.name} Balance: {self.balance}"

jim = User("Jim")
jim.makeDeposit(100)
jim.makeDeposit(500)
jim.makeDeposit(20)
jim.displayBalance()

dwight = User("Dwight")
dwight.makeDeposit(10)
dwight.makeDeposit(1000)
dwight.makeWithdrawal(500)
dwight.displayBalance()

pam = User("Pam")
pam.makeDeposit(400)
pam.makeWithdrawal(10)
pam.makeWithdrawal(50)
pam.makeWithdrawal(30)
pam.displayBalance()

jim.transferBalance(pam, 30)