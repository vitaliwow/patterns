def outer_function():
    x = 10  # (enclosing)
    print("original value of x:", x)

    def inner_function():
        nonlocal x  # as nonlocal
        x = 20  # changing the value of x

    inner_function()
    print("Value changed with nonlocal:", x)


if __name__ == "__main__":
    outer_function()