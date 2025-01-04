"""We can describe the protocol of the constructor, which should be implemented by a class to create instances.

Protocols describe the behavior that a class should support.
"""

from typing import Protocol, Type


class ConstructorProtocol(Protocol):
    def __init__(self, name: str, age: int) -> None:
        ...

    def cry(self) -> None:
        ...


# class is accorded to the protocol (implements the __init__ method and its signature)
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def cry(self) -> None:
        print("Person is crying")

# class is accorded to the protocol too
class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def cry(self) -> None:
        print("Animal is crying")

    def __repr__(self) -> str:
        return f"Animal(name={self.name}, age={self.age})"


# class isn't accorded to the protocol
class Car:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Car(name={self.name})"

    def make_noise(self) -> None:
        # car can't cry
        print("Car is making noise")

def create_instance(cls: type(ConstructorProtocol), *args) -> ConstructorProtocol:
    return cls(*args)


if __name__ == "__main__":
    person = create_instance(Person, "Alice", 30)
    animal = create_instance(Animal, "Fluffy", 5)

    person.cry()
    animal.cry()

    car = create_instance(Car, "BMW")
    car.cry()  # raises AttributeError: 'Car' object has no attribute 'cry'. Mypy will catch this error before the build