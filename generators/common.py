"""Generators - objects to create lazy sequences.

They return single value for the time with stopping evaluations between calls
Also, they use a keyword `yield` to return values

Key differences are:
- lazy evaluations: items could be created on demand.
    That allows to use resources (memory) in more efficient way for big sequences
- supports iteration protocol: generators must define methods iter and next
- function with `yield` keyword returns generator object
"""
from typing import Generator


# simple generator func
def count_up_to(max_value: int) -> Generator:
    count = 1
    while count <= max_value:
        yield count # on every `yield` call the func stops and then starts from the breakpoint on demand
        count += 1

def iterate_over(num: int) -> None:
    for number in count_up_to(num):
        print(number)

def gen_as_iter(num: int) -> None:
    """Generator could work as iterator"""
    gen = count_up_to(num)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))

def gen_expression(num: int) -> None:
    """Example of generator expression"""
    sqr = (x**2 for x in range(num))

    for i in range(num):
        print(next(sqr))


if __name__ == "__main__":
    iterate_over(6)
    print("_____________")
    gen_as_iter(5)
    print("_____________")
    gen_expression(4)

