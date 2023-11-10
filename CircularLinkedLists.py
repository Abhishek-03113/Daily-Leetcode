class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None



class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        newNode = Node(data)
        cur = self.head
        newNode.next = self.head

        if not self.head:
            newNode.next = newNode
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode

        self.head = newNode

    def append(self, data):
        if not self.head:
            self.head = Node(data) 
            self.head.next = self.head
        else:
            newNode = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)

            cur = cur.next

            if cur == self.head:
                break


test = CircularLinkedList()

test.append("A")
test.append("B")
test.append("C")

test.print_list()

test.prepend("Z")

test.print_list()
