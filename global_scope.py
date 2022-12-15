animal = "Lemur"

print("OUTSIDE OF FUNCTION", animal)

def func():
    print("INSIDE FUNCTION", animal)
    def inner_func():
        print("INNER FUNCTION, animal")
    inner_func()
func()

# In globlal scope, the variable  works inside or outside of function.