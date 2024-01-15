import math
from typing import List


class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        
        def f(i, total, cost, dp):
            if i == n or total <= 0:
                return 0
            if (i,total) in dp:
                return dp[(i, total)]
            dp[(i,total)] = max(1 + f(i + 1, math.floor(total - (10 / 100 * cost[i])), cost, dp) if cost[i] <= total else 0, f(i + 1, total, cost, dp))
            return dp[(i,total)]
        dp = {}
        
        
        
        return f(0, total, cost, dp)
            
        
import math
from typing import List


class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        dp = [0 for _ in range(total + 1)]
        for c in reversed(cost):
            for t in range(total, c-1, -1):
                dp[t] = max(dp[t], dp[t - (c + 9)//10] + 1)
        return dp[total]
