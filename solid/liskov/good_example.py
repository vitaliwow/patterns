"""Subdivision into subtypes allows for correct use of replacement"""

from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        print("I can fly!")

class NonFlyingBird(Bird):
    def move(self):
        print("I can walk!")

class Penguin(NonFlyingBird):
    pass
