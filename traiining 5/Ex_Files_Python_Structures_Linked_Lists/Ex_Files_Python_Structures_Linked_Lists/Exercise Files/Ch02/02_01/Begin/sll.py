# single linked List. uses only availible next pointer .
# node have single point connecting them,

# douhble linked list allow to move between back and forth items in the linked list


# entry point of link list is called Head
# the emd point of linked list point to none which is the end node

# linear data structure.

# operations. Add and remove nodes at begining and end.

# add before and after (key).


class SingleLinkedListNode:

    def __init__(self, data):
        self._data = data
        self._next = None

    def __repr__(self) -> str:
        return "Single Linked List Node {}".format(self._data)

    def getData(self):
        return self._data

    def setData(self, new_data) -> None:
        self._data = new_data

    def getNext(self):
        return self._next

    def setNext(self, new_value) -> None:
        self._next = new_value


class DoubleLinkedListNode:

    def __init__(self, data):
        self._data = data
        self._next = None
        self._previous = None

    def __repr__(self) -> str:
        return "Double Linked List Node {}".format(self._data)

    def getData(self):
        return self._data

    def setData(self, new_data) -> None:
        self._data = new_data

    def getNext(self):
        return self._next

    def setNext(self, new_value) -> None:
        self._next = new_value

    def setPrevious(self, new_value) -> None:
        self._previous = new_value

    def getPrevious(self):
        return self._previous


# single linked List class
class SSL:

    def __init__(self):
        self._head = None
        self._end_point = None

    def __repr__(self) -> str:
        return "SSL {}".format(self._head)

    def isEmpty(self):
        # if self._head is None:
        #     return True
        # else:
        #     return False

        # same code
        return self._head is None

    def addFront(self, new_data) -> None:
        holder = SingleLinkedListNode(new_data)
        holder.setNext(self._head)
        self._head = holder

    def getHead(self):
        return self._head

    def size(self):
        size = 0
        if self._head is None:
            return 0

        current = self._head

        while current is not None:  # while there are nodes to count
            size += 1
            current = current.getNext()

        return size

    def search(self, value):
        if self._head is None:
            return "Linked Lst Empty"

        current = self._head

        while current is not None:  # while there are nodes to count

            # nodes data matches what we are looking
            if current.getData() is value:
                return True

            else:
                # Data does not match
                current = current.getNext()

        return False

    def remove(self, value):
        """Removes the first occurence of
         the node """
        if self._head is None:
            return "Linked Lst Empty"

        current = self._head
        previous = None
        found = False

        while not found:
            if current.getData is value:
                found = True
            else:
                if current.getNext() is None:
                    return "Not found element"

                else:
                    previous = current
                    current = current.getNext()

        if previous is None:
            self._head = current.getNext()
        else:
            previous.setNext(current.getNext())


def main():
    node = SingleLinkedListNode("text")

    node.getData()

    print(node.getData())

    node.setData("new Data")

    print(node.getData())

    node2 = SingleLinkedListNode("lori")

    node.setNext(node2)
    print(node.getNext())

    nodeDouble = DoubleLinkedListNode(1)
    nodeDouble2 = DoubleLinkedListNode(2)

    nodeDouble.getPrevious()
    print(nodeDouble.getPrevious())

    nodeDouble.setPrevious(nodeDouble2)
    print(nodeDouble.getPrevious())

    ssl = SSL()
    print(ssl.isEmpty())

    ssl.addFront("test")
    print(ssl.getHead())

    ssl.addFront("other")

    print(ssl.size())

    print(ssl.search("lk"))

    print(ssl.search("test"))

    ssl.addFront(2)
    ssl.addFront(4)


    ssl.remove("test")
    print(ssl.search("test"))


if __name__ == "__main__":
    main()
