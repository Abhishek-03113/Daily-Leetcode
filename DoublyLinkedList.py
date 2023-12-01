class Node:
    def __init__(self,data):
        self.data = data 
        self.prev = None
        self.next = None 


class DoublyLinkedList:

    def __init__(self):
        self.head = None
    
    def append(self,data):
        if self.head is None: 
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data) 
            curr = self.head 

            while curr.next:
                curr = curr.next 
            curr.next = newNode 
            newNode.prev = curr 

    def prepend(self,data):
        if self.head is None:
            newNode = Node(data) 
            self.head = newNode 
        else:
            ## prepend means before the head node so  
            newNode = Node(data)
            cur = self.head 
            cur.prev = newNode 
            newNode.next = cur
            self.head = newNode


    def print_list(self):
        cur = self.head 
        while cur: 
            print(cur.data) 
            cur = cur.next 
    
