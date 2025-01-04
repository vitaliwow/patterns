"""Is usd to managing access to class attrs

__get__(self, instance, owner): returns value
__set__(self, instance, value): sets value
__delete__(self, instance): deletes value
"""

class MyDescriptor:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        print("getting value")
        return self.value

    def __set__(self, instance, value):
        print("setting value")
        self.value = value


class MyClass:
    attr = MyDescriptor()


if __name__ == "__main__":
    obj = MyClass()
    obj.attr = 42
    print(obj.attr)
