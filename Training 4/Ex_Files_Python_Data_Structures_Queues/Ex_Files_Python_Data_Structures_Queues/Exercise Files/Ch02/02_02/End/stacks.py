class Stack:

    # it is a data structure that stores items in the ordr these were added.
    # item can be added or removed from the top of the stack *(Last in First out)

    def __init__(self):
        self.items = []  # initialise this to an emptyt list to hold the components

    def push(self, item):

        self.items.append(item)

    def pop(self):

        if self.items:  # to check that there is at least one element in the list.
            return self.items.pop()
        return None

    # see what item is going to be removed and return that as well.
    # return the last object in the list which is also the  item at the top of the stack
    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):  # return the size opf the object
        return len(self.items)

    def is_empty(self):
        return self.items == []


def main():
    created_stack = Stack()
    created_stack.push("lol")
    created_stack.push("lmao")

    print(created_stack.items)

    popped = created_stack.pop()
    print(f"Popped Object \t {popped}")
    print(created_stack.items)

    created_stack.push("lol")
    created_stack.push("lmao")
    print(created_stack.items)

    peeked = created_stack.peek()
    print(f"peeked Object \t {peeked}")

    size = created_stack.size()
    print(f"Size Object \t {size}")

    checker_Items = created_stack.is_empty()
    print(f"checker empty Object \t {checker_Items}")


if __name__ == "__main__":
    main()
