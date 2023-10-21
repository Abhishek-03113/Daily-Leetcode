class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        # if linked list is empty set head to the new node
        if self.head is None:
            self.head = newNode

            return

        # non empty linked list
        # search for node with next pointer to null

        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next

        # append the new element at end of linked list
        lastNode.next = newNode

    # Print the Linked List
    def printList(self):
        currNode = self.head

        while currNode:
            print(currNode.data, "==>", end="")
            currNode = currNode.next

    # insert at the start of the LL

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head

        self.head = newNode

    # Insert a node after Nodes
    # To insert at a specific position need use loop to find the node
    def insertAfterNode(self, prevNode, data):
        if not prevNode:
            print("No previous node found")
            return
        newNode = Node(data)

        newNode.next = prevNode.next
        prevNode.next = newNode


linkedList = LinkedList()

linkedList.append("A")
linkedList.append("B")
linkedList.append("C")
linkedList.append("D")
linkedList.append("E")
linkedList.prepend("F")
linkedList.insertAfterNode(linkedList.head.next, "Q")


linkedList.printList()
