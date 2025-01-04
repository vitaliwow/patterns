"""Describes a collection behavior such as lists, sets, dicts

__contains__(self, item): checks if an element contains in the collection ('in' operator).
__len__(self): returns the collection length.
__iter__(self): returns an iterator.
"""

class MyContainer:
    """Collection or Container Protocol"""
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        return item in self.data

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)


if __name__ == '__main__':
    container = MyContainer([1, 2, 3])
    print(2 in container)  # True
    print(len(container))  # 3
