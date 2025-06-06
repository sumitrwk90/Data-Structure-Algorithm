
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def push_back(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node

        else:
            current = self.tail
            current.next = new_node
            self.tail = new_node

    def printll(self):
        current = self.head
        while current != None:
            print(current.data, end="->")
            current = current.next

        print(None)


ll = LinkedList()

ll.push_front(5)
ll.push_front(4)
ll.push_front(3)
ll.push_front(2)

ll.push_back(10)
ll.push_back(9)
ll.push_back(8)
ll.push_back(7)

print(ll.printll())
