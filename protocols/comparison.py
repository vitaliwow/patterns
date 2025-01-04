"""Describes how objects could be compared

__eq__(self, other): equivalence (==).
__ne__(self, other): non-equivalence (!=).
__lt__(self, other): less than (<).
__le__(self, other): less than or equal (<=).
__gt__(self, other): greater (>).
__ge__(self, other): greater or equal (>=).
"""

class MyComparable:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


if __name__ == "__main__":
    a = MyComparable(10)
    b = MyComparable(20)
    print(a == b)  # False
    print(a < b)   # True
