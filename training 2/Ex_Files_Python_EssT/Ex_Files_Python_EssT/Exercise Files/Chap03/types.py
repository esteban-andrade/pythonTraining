#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# # x = "Seven".upper()
# # x = "seven {0:<9} {1:>9}".format(2,3)
# a=8
# b=9
# x = f"seven {a:<9} {b:>9}"
# print('x is {}'.format(x))
# print(type(x)) # type of value/variable

from decimal import *

a = Decimal(".10")
b=Decimal(".30")
x=a+a+a-b
print('x is {}'.format(x))
print(type(x))  # type of value/variable
print(id(x))

b = (1, 2, 3, 4, 5)
d = (1, 2, 3, 4, 5)


if b[0] is d[0]:
    print("is used")

if isinstance(b,tuple): # to check types 
    print(True)
else:
    print("Nop")