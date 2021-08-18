#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# how we import a module

import sys


import os

from random import randint

import datetime 

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))

    plat = sys.platform
    print(plat)

    os_name = os.name
    print(os_name)

    path = os.getenv("PATH")
    print(path)

    current_dir = os.getcwd()
    print(current_dir)

    random = os.urandom(2).hex() # will get a byte object for hex use .hex
    print(random)

    randi = randint(1,100)

    print(randi)

    now = datetime.datetime.now()
    print(now)




if __name__ == '__main__':
    main()
