import re
from typing import Counter


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

    # Deleting a node

    # Deleting Head Node
    def deleteNode(self, key):
        currNode = self.head

        if currNode and currNode.data == key:
            self.head = currNode.next
            currNode = None

            return

        prev = None

        while currNode and currNode.data != key:
            prev = currNode
            currNode = currNode.next

        if currNode is None:
            return
        prev.next = currNode.next
        currNode = None

    # Deletion By position

    def deleteNodeAtPosition(self, pos):
        if self.head:
            currNode = self.head
            if pos == 0:
                self.head = currNode.next
                currNode = None

        prev = None
        count = 0

        while currNode and count != pos:
            prev = currNode
            currNode = currNode.next

            count += 1

        if currNode is None:
            return

        prev.next = currNode.next
        currNode = None

    def lenIterative(self):
        count = 0
        currNode = self.head

        while currNode:
            count += 1
            currNode = currNode.next

        return count

    def lenRecursive(self, node):
        if node is None:
            return 0
        return 1 + self.lenRecursive(node.next)

    def swapNode(self, key1, key2):
        if key1 == key2:
            return

        prev1 = None
        curr1 = self.head

        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head

        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next

    def reverseIterative(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverseRecursive(self):
        def _reverseRecursive(curr, prev):
            if not curr:
                return prev
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

            return _reverseRecursive(curr, prev)

        self.head = _reverseRecursive(curr=self.head, prev=None)

    def MergeSort(self, llist):
        p = self.head

        q = llist.head

        s = None

        if not p:
            return q

        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p

                p = s.next
            else:
                s = q

                q = s.next

            newHead = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next

            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = newHead

        return self.head

    def removeDuplicates(self):
        curr = self.head
        prev = None

        dups = dict()

        while curr:
            if curr.data in dups:
                prev.next = curr.next
                curr = None
            else:
                dups[curr.data] = 1
                prev = curr

            curr = prev.next


linkedList = LinkedList()

linkedList.append("A")
linkedList.append("B")
linkedList.append("C")
linkedList.append("D")
linkedList.append("E")
linkedList.prepend("F")
linkedList.insertAfterNode(linkedList.head.next, "Q")

print(f"Linked List before reversing : \n")
linkedList.printList()
print("\n")
print(f"Linked List after Iterative Reversing :\n ")
linkedList.reverseIterative()
linkedList.printList()
print("\n")

print(f"Linked List after Recursive Reversing : \n")
linkedList.reverseRecursive()
linkedList.printList()
