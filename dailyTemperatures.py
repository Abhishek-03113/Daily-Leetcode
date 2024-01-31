from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Given : array of integers temperatures 
        Return : array of no. of days to wait after i'th day to get warmer 
        """

        n = len(temperatures)

        q = deque() 

        res = [0] * n 

        for i in range(n-1, -1,-1):

            if not q:
                q.appendleft(i)
                res[i] = 0 
            
            else:

                while q and temperatures[i] >= temperatures[q[0]]:
                    q.popleft()
                
                if not q:
                    res[i]  = 0 

                else:
                    res[i] = q[0] - i 
                
                q.appendleft(i)
                
        return res


