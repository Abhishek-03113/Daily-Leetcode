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

    def removeNode(self, key):
        if self.head:
            if self.head.data == key:
                cur = self.head

                while cur.next != self.head:
                    cur = cur.next

                if self.head == self.head.next:
                    self.head = None

                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head

                prev = None

                while cur.next != self.head:
                    prev = cur
                    cur = cur.next

                    if cur.data == key:
                        prev.next = cur.next
                        cur = cur.next


test = CircularLinkedList()

test.append("A")
test.append("B")
test.append("C")

print("### Append ###")
test.print_list()
test.prepend("Z")
print("### Prepend ###")
test.print_list()


test.removeNode("C")
print("### Remove ###") 
test.print_list()
