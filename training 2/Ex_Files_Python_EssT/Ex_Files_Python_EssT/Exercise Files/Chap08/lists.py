#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ] # list it is sequential and iterable\

    print(game[1:3:2])

    # search in a list 
    i = game.index("Paper")
    print (game[i])

    # append

    game.append("Computer") # similar to push back

    # insert
    game.insert(0,"Insert") # put location and object 

    #Remove
    game.remove("Paper")  # pop c we can use pop or del (delete)

    #join list to joint strings

    print(",".join(game))

    # to obtain len we can use len
    len(game)


    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()


# List are mutable and tuple are not