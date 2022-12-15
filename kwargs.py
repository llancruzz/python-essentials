def print_ages(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} is {v} years old")
    
print_ages(max=67, sue=59, kim=14)