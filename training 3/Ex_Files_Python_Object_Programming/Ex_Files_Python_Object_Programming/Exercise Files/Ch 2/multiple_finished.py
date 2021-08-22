# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"

# multiple inheritance


class C(B, A):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        # will print the value of the class that is first in this case from class B
        print(self.name)


# create the class and call showname()
c = C()

# wil allow to ispect the values from inheritance 
print(C.__mro__)
c.showprops()
