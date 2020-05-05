import store
import product

costco = store.Store("Costco")
tp = product.Product("toilet paper", 10, "essentials")
flour = product.Product("flour", 15, "essentials")
beer = product.Product("beer", 30, "essentials")

costco.addProducts(tp).addProducts(flour).addProducts(beer)

costco.sellProduct(tp.id)
costco.sellProduct(5)

beer.inflation(.2)
print(beer.printInfo())

costco.setClearance("essentials", .5)