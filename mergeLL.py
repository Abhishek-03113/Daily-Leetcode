

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def reverse(self, r):
    
    prev = None 
    curr = r 
    
    while curr:
        nxt = curr.next 
        curr.next = prev 
        prev = curr 
        curr = nxt 
    
    return prev

class Solution:
    def mergeResult(self, h1, h2):
        
        t = Node(0) 
        
        curr = t
        
        while h1 or h2: 
            
            if h1 is None:
                curr.next = h2 
                break 
            elif h2 is None: 
                curr.next = h1 
            
                break 
            
            if h1.data <= h2.data:
                curr.next = h1 
                h1 = h1.next
            else:
                curr.next = h2 
                h2 = h2.next
            
            curr = curr.next 
        
        prev = None 
        curr = t.next 
        
        while curr: 
            nxt = curr.next  
            curr.next = prev 
            prev = curr
            curr = nxt 
        return prev