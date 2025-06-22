import math
import os
import sys
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce
mod = 10**9 + 7


def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    pre = [0] * (n + 1)

    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + a[i - 1]

    ans = float('inf')
    
    summ = float('inf') 
    
    for i in range(k, n + 1): 
        
        curr = pre[i] - pre[i - k] 
        
        if curr < summ: 
            summ = curr 
            ans = i - k + 1
        # print(pre[i] - pre[i - k], i - k + 1)  
    print(ans)
        
solve()
