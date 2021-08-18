#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = '47'
y = int(x)
# float is to change to floar
# abs to get absolute value
#divmod return a tuple with the result of division and remainder 
z = divmod(y,3)
#complex is to change to complex numberand j is the imaginary part 

w = complex(y,3) # or y+3j 

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')
print(f'z is {type(z)}')
print(f'z is {z}')
print(f'w is {type(w)}')
print(f'w is {w}')
