#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from math import pi

def main():
    seq = range(11)
    seq2 = [x *2 for x in seq]
    seq2 = [round(pi,i) for i in seq]
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()


#x**2 x squared x^2
