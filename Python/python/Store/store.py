class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def addProducts(self, product):
        self.products.append(product)
        print(f"Added {product.printInfo()} to the store")
        return self

    def sellProduct(self, id):
        for i in range(len(self.products)):
            if self.products[i].id == id:
                print(f"Removing the product {self.products[i].printInfo()}")
                self.products.pop(i)
                return self
        else:
            print(f"No product with the id:{id}")
        return self

    def setClearance(self, category, percentDiscount):
        for product in self.products:
            if product.category == category:
                product.updatePrice(percentDiscount, False)
                print(f"Discounted item {product.printInfo()}")
