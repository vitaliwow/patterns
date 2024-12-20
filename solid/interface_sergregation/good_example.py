"""Classes should not depend on interfaces that they do not use.

If an interface becomes too large and contains methods that are not needed by all of its implementations,
it should be split into smaller interfaces.
"""
from abc import ABC, abstractmethod


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Human(Workable, Eatable):
    def work(self):
        print("I work!")

    def eat(self):
        print("I eat!")


class Robot(Workable):
    def work(self):
        print("I work!")
