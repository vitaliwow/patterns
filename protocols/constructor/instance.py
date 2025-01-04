"""The protocol describes how objects are created and initialized.

Main methods are:
    __new__(cls, *args, **kwargs): responsible for creating a new object.
    __init__(self, *args, **kwargs): responsible for initializing an object after its creation.
"""


class MyClass:
    """In context of instance creation

     __new__ method is called first, then __init__ method is called.
    """

    def __new__(cls, *args, **kwargs):
        print("Object creation")
        return super().__new__(cls)

    def __init__(self, value):
        print("Object initialization")
        self.value = value


if __name__ == "__main__":
    # In context of instance creation
    obj = MyClass(42)
