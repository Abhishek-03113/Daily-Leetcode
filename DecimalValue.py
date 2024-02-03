

'''

class node:

    def __init__(self):

        self.data = None

        self.next = None

'''



class Solution:

    def decimalValue(self, head):

        MOD=10**9+7

        s = "" 

        

        while head: 

            s = s + str(head.data)

            

            head = head.next 

        

        return int(s,2) % MOD

        # Code here

