x = 10  # Global


def outer_function():
    x = 20  # (enclosing)

    def inner_function():
        x = 30
        print("1. Local: ", x)

    inner_function()
    print("2. Enclosing: ", x)

outer_function()
print("3. Global: ", x)
