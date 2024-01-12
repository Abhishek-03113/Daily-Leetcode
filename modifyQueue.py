class Solution:

    def modifyQueue(self, q, k):

        if k == 1:

            return q 

        

        else:

            

            n = len(q) 

            

            first_k = q[:k][::-1]

            remaining = q[k:]

            

            return first_k + remaining
