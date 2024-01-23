User function Template for python3

from collections import deque 

class Solution:

    def findOrder(self, n, m, prerequisites):

        # Code here

        """

        Given : n : tasks 

                prerequisites : list of prerequisite pairs

                m : size of prerequisites 

                

            

        return : 

        

                

                find a ordering of tasks to finish all tasks



        """

        

        g = [[] for _ in range(n)]

        in_deg = [0]*n 

        

        for i in prerequisites: 

            

            g[i[1]].append(i[0])

            in_deg[i[0]] += 1 

        

        q = deque() 

        

        ans = []

        

        for i in range(n):

            

            if in_deg[i] == 0: 

                q.append(i)

                ans.append(i)

        

        while q: 

            node = q.popleft() 

            for child in g[node]:

                in_deg[child] -=1 

                

                if in_deg[child] == 0: 

                    q.append(child)

                    ans.append(child)

        

        if len(ans) < n: 

            ans = []

        

        return ans

        
