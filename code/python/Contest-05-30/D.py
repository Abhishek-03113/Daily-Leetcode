# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        carry = 0
        ans = None
        d1 = l1 
        d2 = l2 

        while d1 or d2:
            sm = 0 
            if d1 and d2:
                sm = d1.val + d2.val 
            
            elif d1 and not d2:
                sm += d1.val
            
            else:
                sm += d2.val
            
            prev = ans 

            if carry > 0:
                sm += carry 
            
            if sm >= 10:
                temp = sm 
                sm = temp %10  
                carry = temp // 10 
            
        
            if prev is None:
                ans = ListNode(sm)
            else:
                newNode = ListNode(sm)
                ans.next = newNode 
            
        
            if d1:
                d1 = d1.next 
            
            if d2:
                d2 = d2.next  
            
        return ans


        


            
