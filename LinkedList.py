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

    def nthFromLastNode(self, n):
        total_len = self.lenIterative()

        curr = self.head

        while curr:
            if total_len == n:
                print(curr.data)
                return curr.data

            total_len -= 1

            curr = curr.next

        if curr is None:
            return

    def nthFromLastNode2Pointers(self, n):
        # pointer p will point to head node
        # pointer q will point n pointers beyond head node

        p = self.head
        q = self.head

        if n > 0:
            count = 0

            while q:
                count += 1
                if count >= n:
                    break
                q = q.next

            if not q:
                print(str(q) + "is greaterr than number of nodes in list ")

                return

            while p and q.next:
                p = p.next
                q = q.next
            return p.data
        else:
            return None

    # Iterative Implementations
    def CountOccurence(self, data):
        count = 0

        curr = self.head

        while curr:
            if curr.data == data:
                count += 1
            curr = curr.next

        return count

    def CountOccurencesRecursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.CountOccurencesRecursive(node.next, data)
        else:
            return self.CountOccurencesRecursive(node.next, data)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head

            prev = None
            count = 0

            while p and count < k:
                prev = p

                p = p.next
                q = q.next

                count += 1
            p = prev

            while q:
                prev = q
                q = q.next

            q = prev

            q.next = self.head
            self.head = p.next

            p.next = None

    def isPalindrome(self):
        s = ""
        cur = self.head

        while p:
            s += cur.data
            p = p.next

        return s == s[::-1]

    def isPalindromeStack(self):
        cur = self.head
        stack = []

        while cur:
            stack.append(cur.data)
            cur = cur.next
        cur = self.head

        while cur:
            data = stack.pop()

            if cur.data != data:
                return False
            cur = cur.next

        return True

    def isPalindromeTwoPointer(self):
        if self.head:
            p = self.head  # pointer pointing at head of the linked list
            q = self.head  # pointer pointing at end of the linked list

            prev = []  # for helping q to move to the previous node

            i = 0

            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i - 1]

            count = 1

            while count <= i // 2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True

    def moveTailToHead(self):
        if self.head and self.head.next:
            last = self.head
            second_to_last = None
            while last.next:
                second_to_last = last
                last = last.next
            last.next = self.head
            second_to_last.next = None
            self.head = last

        # tail should be pointing to the head node
        # the previous node to the tail should point to null

    def sumTwoLinkedList(self, llist):
        l1 = self.head
        l2 = llist.head

        resultList = LinkedList()

        carry = 0
        while l1 or l2:
            if not l1:
                i = 0
            else:
                i = l1.data
            if not l2:
                j = 0
            else:
                j = l2.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                resultList.append(remainder)
            else:
                carry = 0
                resultList.append(s)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return resultList


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

print(f"List Before rotation :: \n")
linkedList.printList()

print(f"List after rotation :: \n")
linkedList.rotate(3)
linkedList.printList()
