"""Classes should not depend on interfaces that they do not use.

If an interface becomes too large and contains methods that are not needed by all of its implementations,
it should be split into smaller interfaces.
"""


class Worker:
    def work(self):
        pass

    def eat(self):
        pass


class Human(Worker):
    def work(self):
        print("I work")

    def eat(self):
        print("I eat!")


class Robot(Worker):
    def work(self):
        print("I work")

    def eat(self):
        raise NotImplementedError("Robots do not eat!")
