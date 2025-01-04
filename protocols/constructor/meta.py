"""The protocol describes how classes are created"""


class MyMeta(type):
    """In context of class creation

    __new__ method is called first
    """
    def __new__(cls, name, bases, dct):
        # We can add attributes to the class here
        print(f"Class created {name}")
        return super().__new__(cls, name, bases, dct)

class MyClassWithCustomMeta(metaclass=MyMeta):
    def __init__(self, value):
        self.value = value


if __name__ == "__main__":
    obj_meta = MyClassWithCustomMeta("New class")
    print(obj_meta.value)
