#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''

auth = False
count =0
max_num = 5


while pw != secret:
    count+=1
    if count >= max_num:
        break # will end the loop
    elif count == 4:
        continue
    pw = input(f"{count}What's the secret word? ")
else: # executes if loop ends normally
    auth = True
    print("Authorized")


# continue-->  short cut to start it again