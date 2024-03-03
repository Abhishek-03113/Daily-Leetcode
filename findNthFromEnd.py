# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.findLength(head)
        i, traverseTill = 0, length - n - 1
        if traverseTill == -1:
            return head.next
        curr = head
        while i < traverseTill:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return head

    def findLength(self, head):
        count = 0
        if head is None:
            return count
        curr = head
        while curr is not None:
            count += 1
            curr = curr.next
        return count
