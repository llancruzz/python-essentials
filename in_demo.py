flavors = ["chocolate", "vanilla", "banana", "lemon", "strawberry"]

response = input("What flavor would you like? ")

while response.lower() not in flavors:
    response = input("I don't know that flavor! Try again: ")
    
print(f"Ok, {response} ice cream coming right up!")