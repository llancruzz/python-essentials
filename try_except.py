try:
    num = int(input("Please enter a number: "))
except ValueError:
    print("Oh no, that isn't a number!")
    num = int(input("Please enter only a number: "))

print(f"You entered {num}")