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


    def __len__(self):
        cur = self.head 
        count = 0 

        while cur:
            count += 1
            cur = cur.next 

            if cur == self.head:
                break 
        

        return count 
    
    def split(self):

        size = len(self)

        if size == 0: 
            return None 
        if size == 1:
            return self.head 

        
        mid = size // 2

        count = 0 

        prev = None 

        cur = self.head 

        while cur and count < mid:

            count += 1
            
            prev = cur 

            cur = cur.next 

        
        prev.next = self.head 

        split_list = CircularLinkedList()


        while cur.next != self.head:
            split_list.append(cur.data)
            cur = cur.next 
        
        split_list.append(cur.data)


        self.print_list()

        print("\n")

        split_list.print_list()


    def removeNode(self,node):
        if self.head == node: 
            cur = self.head 

            while cur.next != self.head: 
                cur = cur.next 
            

            if self.head ==self.head.next: 
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

                if cur == node:
                    prev.next = cur.next 
                    cur = cur.next

    
    def josephus_circle(self,step):

        cur = self.head 

        length = len(self)

        while length > 1:

            count = 1

            while count != step:
                cur = cur.next 

                count += 1
            
            print("Kill ", str(cur.data))

            self.removeNode(cur)

            cur = cur.next 

            count -= 1
            
        


test = CircularLinkedList()

test.append("A")
test.append("B")
test.append("C")

print("### Append ###")
test.print_list()
test.prepend("Z")
print("")
print("### Prepend ###")
test.print_list()
print("")

# test.removeNode("C")
# print("### Remove ###") 
# test.print_list()


test.split()


print("")

print("Length of the linked list is ",len(test))