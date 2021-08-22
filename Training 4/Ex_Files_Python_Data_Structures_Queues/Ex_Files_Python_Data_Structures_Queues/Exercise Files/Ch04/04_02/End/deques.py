class Deque:

    def __init__(self):
        self.items = []

    def push_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def pop_front(self):

        if self.items():
            return self.items.pop(0)
        return None

    def pop_back(self):
        if self.items():
            return self.items.pop()  # or -1 index
        return None

    def front(self):

        if self.items():
            return self.items[0]
        return None

    def back(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):

        return self.items == []

    def at(self, index):
        if self.items():
            return self.items[index]  # or -1 index
        return None

    def insert(self, index, element):
        if self.items():
            self.items.insert(index, element)  # or -1 index
        return None


# refer to this https://www.cplusplus.com/reference/deque/deque/
