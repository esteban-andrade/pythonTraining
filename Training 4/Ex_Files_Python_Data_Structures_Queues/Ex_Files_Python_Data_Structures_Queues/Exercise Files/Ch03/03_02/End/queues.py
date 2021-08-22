class Queue:
    # a queu stores the items in the order that they were added.
    # items are added at the back and removed at the front of the queue
    # the order is preserved in the queue

    # queue is stored in a list
    def __init__(self):
        self.items = []

    def enqueue(self, item):  # similar to push front
        self.items.insert(0, item)

    def dequeue(self):  # similar to pop
        if self.items:
            return self.items.pop()
        return None

    def push(self,items):
        self.items.append(items)


    def pop(self):
        if self.items:
            return self.items.pop(0)
        return None

    def peek(self): # similar to back in c++ 
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


def main():
    queue = Queue()
    

if __name__ == "__main__":
    main()
