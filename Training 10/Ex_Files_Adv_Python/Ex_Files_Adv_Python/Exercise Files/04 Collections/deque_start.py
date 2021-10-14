# deque objects are like double-ended queues

import collections
import string


def main():
    
    # TODO: initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # deques support the len() function
    print("Item count: " + str(len(d)))

    # TODO: deques support the len() function
    for elem in d:
        print(elem.upper(), end=",")

    # TODO: deques can be iterated over
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)


    # TODO: manipulate items from either end

    print(d)
    d.rotate(10)
    print(d)

    # TODO: rotate the deque


if __name__ == "__main__":
    main()
