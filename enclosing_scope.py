def outer():
    animal = "Secretary Bird"
    print("INSIDE OUTER FUNC: ", animal)

    def inner():
        print("INSIDE INNER FUNC: ,", animal)

        def third():
            print("INSIDE THIRD NESTED FUNC: ", animal)
        third()
    inner()


outer()
