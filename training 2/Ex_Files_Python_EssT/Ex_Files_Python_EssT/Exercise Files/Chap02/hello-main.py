#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print ("\n Lines 2") 

# if __name__ == '__main__': main()
if __name__ == "__main__":
    main()
