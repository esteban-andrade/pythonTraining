#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is a long string with a bunch of words in it.'
print(s)

#split will separate the string 
print(s.split()) # this will change to a list

l = s.split()

s2 =" : ".join(l)
# we
print(s2)