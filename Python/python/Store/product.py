import uuid

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.id = uuid.uuid4()

    def updatePrice(self, percentChange, isIncreased):
        if(isIncreased):
            self.price *= 1+percentChange
        else:
            self.price *= 1-percentChange
        return self
    
    def printInfo(self):
        return f"{self.name} ${self.price:.2f} {self.category} id:{self.id}"

    def inflation(self, percentIncrease):
        self.updatePrice(percentIncrease, True)
        return self