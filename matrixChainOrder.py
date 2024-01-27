from math import inf

class Solution:

    def matrixChainOrder(self, p, n):

        cost = [[inf for j in range(n)] for i in range(n)]

        bracket = [['' for j in range(n)] for i in range(n)]

        

        for i in range(n-1):

            cost[i][i+1] = 0 

            bracket[i][i+1] = chr(ord('A') + i)

        

        for c in range(2, n):

            for i in range(n-c):

                j = i + c

                for k in range(i+1, j):

                    if cost[i][j] > cost[i][k] + cost[k][j] + p[i] * p[j] * p[k]:

                        cost[i][j] = cost[i][k] + cost[k][j] + p[i] * p[j] * p[k]

                        bracket[i][j] = '(' + bracket[i][k] + bracket[k][j] + ')'



        return bracket[0][n-1]
