prices = {
    "arugala": 1.10,
    "basil": 2.54,
    "blackberries": 2.88,
    "coconut": 7.15,
    "fennel": 3.36
}

product = input("What product are you buying? ")
price = prices.get(product)

if price:
    print(f"{product} is ${price}")
else:
    print("I don't have that today, sorry!")