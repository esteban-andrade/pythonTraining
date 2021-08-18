#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('berlin.jpg', 'rb')
    outfile = open('berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240) # select buffer size to be size 10 kb 
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else:
            break
    outfile.close()
    print('\ndone.')


if __name__ == '__main__':
    main()
