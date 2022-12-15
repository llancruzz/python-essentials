def get_total(price, qtd=1, tax=0.03, discount=0):
    subtotal = price * qtd * (1 - discount)
    print(subtotal * (1 + tax))

get_total(5, 3, 0.03, 2)
get_total(price=5, qtd=3, tax=0.03, discount=2)
get_total(price=5, discount=2, tax=0.03, qtd=3)
get_total(5, 3, discount=2)