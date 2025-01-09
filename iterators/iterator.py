"""Iterator it is an object which supports iteration protocol

He realizes an interface for subsequent access to the object elements (list, tuples, etc.)
without showing inner structure

__iter__(): returns iterator.
__next__(): returns next element of the sequence or raises StopIteration exception in case that
the elements aren't available."""


class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            print("Stop Iteration exception raised")
            raise StopIteration
        self.current += 1
        return self.current - 1


if __name__ == "__main__":
    counter = Counter(1, 5)
    for number in counter:
        print(number)  # 1 2 3 4 5

