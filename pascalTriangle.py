import math
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        k = rowIndex 
        n = k+1

        sol = [0] * n

        i = n-2 

        sol[n-1] = 1 

        while (i>=0):

            for j in range(n-1):
                sol[j] += sol[j+1];

            i -= 1

        print(sol)


test = Solution()
test.getRow(3)

