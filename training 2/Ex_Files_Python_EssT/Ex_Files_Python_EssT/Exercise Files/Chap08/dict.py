#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():

    #constructor for dictionary and its the same

    dictio = dict(kitten = "mewuw",dig ="guo")

    for k,v in dictio.items():
        print(f"{k}:{v}")

    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }

    animals["monkey"]="haha" # to add more value

    
    print_dict(animals)

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')

if __name__ == '__main__': main()
