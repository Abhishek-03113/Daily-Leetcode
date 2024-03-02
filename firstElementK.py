#User function Template for python3

from collections import Counter, defaultdict 



class Solution:

    def firstElementKTime(self, n, k, a):

        res = {}

        for i in range(n):

            if res.get(a[i]) and res[a[i]] + 1 == k:

                return a[i]

            elif res.get(a[i]):

                res[a[i]] += 1

            else:

                res[a[i]] = 1

        return -1 

        

        
