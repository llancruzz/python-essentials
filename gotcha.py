def add_thrice(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    lst.append(val)
    return lst

print(add_thrice(99, [1,2,3]))
