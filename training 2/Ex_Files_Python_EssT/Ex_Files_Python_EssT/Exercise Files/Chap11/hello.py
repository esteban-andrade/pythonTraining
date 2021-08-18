#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')

# strings are object and can be called their respective methods
print('Hello, World.'.upper())


#methods for strings.
# .upper() for all letters in uppercase   
# .lower()  for all lower case
# .capitalize() to use upper case in only the first letter 
# title () capitalises letter of each word
# . swap(0 changes upper case to lowercase and viceversa
# .casefold() is similar to lower but more aggressive (includes unicode)
# strings are not mutable.


#formating strings.
x= 42
y = 75
print('Hello, World. {} {}' .format(x,y) )

# 1 and zero and position arguments and can be used to change order 
print('Hello, World. {1} {0}' .format(x, y))

#formating arguments are specified by :
print('Hello, World. {:<5} {:>05}' .format(x, y))

a = x*y
print('Hello, World. {:,}' .format(a))  # to change coma to dor we can add .replace (",",".")

# to change coma to dor we can add .replace (",",".")
print('Hello, World. {:.3f}' .format(a))  # the f is for decimal places .3 (3 decimal places)

# we can use f at the start instead of format as it is more modern.
print(f'Hello, World. {x:.3f}')
