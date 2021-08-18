#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # open only on read mode  r is read only mode    w --> if its write mode mif open in write mode empties the file if its not empty and writes over. if it does not exitst it creates one
    #a --> apend mode similar to w but does not delete content nor creates a new file
    # r+ will allow to reead and write. We can add b or t next to it to say if it is binary or text file
    f = open('lines.txt', "r+")
    for line in f:
        # rstrip will remove any 3white spaces from end of line
        print(line.rstrip())


if __name__ == '__main__':
    main()
