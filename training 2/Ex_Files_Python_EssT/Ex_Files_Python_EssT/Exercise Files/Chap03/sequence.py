#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = [ 1, 2, 3, 4, 5 ]
# x[2]=42
# for i in x:
#     print('i is {}'.format(i))

x = (1, 2, 3, 4, 5) # tupele
x = range(5) # seQUENCE OF 5 NUMBERS
for i in x:
    print('i is {}'.format(i))

z= list(range(5,40,5))

#dictionary
d = {"one":1, "two":2, "three":3,"four": 4,"five": 5}

for i,j in d.items():
    print('i {}, j {}'.format(i,j))
