"""Iterable or iterator

Iterable object it is an object that realizes __iter__ which returns iterator.
Iterator - an object which realizes methods __iter__ and __next__
"""
import typing


class MyIterable:
    """Iterable object with iter method

    Iter methods managing iteration over the given iterable object from items
    """
    def __init__(self, items: typing.List[int] | typing.Tuple[int]) -> None:
        self.items = items

    def __iter__(self) -> typing.Iterator:
        """Iterator - an object which handling sequences to return next item from sequence"""
        return MyIterator(start=0, end=len(self.items) - 1, items=self.items)

class MyIterator:
    """Iterator defines iter and next dunder methods

    The methods handle iteration (iter method with returning self)
    and returning the next item from sequence (next method with raising StopIteration)
    """

    def __init__(self, start: int, end: int, items: typing.List[int] | typing.Tuple[int]) -> None:
        self.current = start
        self.end = end
        self.items = items

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.items[self.current - 1]


if __name__ == "__main__":
    my_iterable = MyIterable([10, 20, 30, 50, 100])
    for index in my_iterable:
        print(index)
