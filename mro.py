class A:
    def show(self):
        print("Class A method")

class B(A):
    def show(self):
        print("Class B method")
        super().show()

class C(A):
    def show(self):
        print("Class C method")
        super().show()

class D(B, C):
    def show(self):
        print("Class D method")
        super().show()

obj = D()
obj.show()
print(D.mro())
