#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'Hello, World.'

# repr --> will print string itself (best possinle string representation )
print(repr(s))


class bunny:
    def __init__(self, n) -> None:
        self._n = n

    # def __init__(self,n):
    #     self._n = n

    # stgring representation from class
    def __str__(self) -> str:
        return f"str: num of pass is {self._n}"

    def __repr__(self) -> str:
        return f"repr: num of pass is {self._n}"


a = bunny(90)
x = bunny(s)
print(x)

print(ascii(x))
# https://mypy.readthedocs.io/en/stable/class_basics.html
# ord gives number of character and chr gives charcater of number


# container

x = (1, 2, 3, 4, 5)
y = len(x)  # len gives number of elements
y = reversed(x)  # will provide with an iterator
y = list(reversed(x))  # wll provide with a reversed list
y = sum(x, 10)  # sum will provide wit the sum of elements we can add number to it
# there is max and min function
# any will give tru if any of the elements are true
# all will return true if all of them are true
# zip works like a pair and we can add values and it will reutn an iterator

a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 10)
z = zip(a, b)

for i, j in z:
    print(f"{i} {j}")
print(x)
print(y)


# numberate can be used to retriebe the order of thinghs
for q, w in enumerate(a):
    print(f"{q} --{w}")

    # isinstance can be used to see if an object is the instance of a class
    # id is the memoru address ID of the object
