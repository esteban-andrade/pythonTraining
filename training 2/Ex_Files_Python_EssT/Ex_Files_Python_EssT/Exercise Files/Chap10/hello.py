#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys

def main():

    try:
        x = 5/0
    except ValueError:
        print("value error")
    # except ZeroDivisionError:
    #     print("dont div by ero")
    except:
        print("unknown",sys.exc_info())

    else:
        print("allg ")


if __name__ == '__main__':
    main()
