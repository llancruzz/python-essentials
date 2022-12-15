# to create a tuple, we have to use parentheses 
dishes = ("burrito", "taco", "fajita", "quesadilla")

# to access tuple
dishes[2]
# 'fajita' 

# to slice tuple
dishes[1:3]
# ('taco', 'fajita')

# index
dishes.index("taco")
# 1

# using IN
"nachos" in dishes
# False

# iterate tuple
for dish in dishes:
    print(dish)

