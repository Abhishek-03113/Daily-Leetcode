"""
@Abhishek 
Day 18 
Topic :  Linked List 
Merging two sorted linked list using two pointer 

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        p = list1
        q = list2
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.val <= q.val:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
        newHead = s

        while p and q:
            if p.val <= q.val:
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
