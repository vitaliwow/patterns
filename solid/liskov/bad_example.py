"""Child object should be able to change by a base class without changes in program behavior"""

class Bird:
    def fly(self):
        print("I can fly!")

class Penguin(Bird):
    """Penguin can't be correctly changed because it rewrites method"""
    def fly(self):
        raise NotImplementedError("Penguins can't fly")
