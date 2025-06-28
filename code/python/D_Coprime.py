import math
import os
import sys
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce
mod = 10**9 + 7

def io():
    return map(int, input().split())


def iol():
    return list(map(int, input().split()))


def ios():
    return input().strip()


def ioi():
    return int(input().strip())


def iom(n, m):
    return [list(map(int, input().split())) for _ in range(n)]



def solve():
    n = ioi() 
    a = iol() 
    
    d = [[] for _ in range(1001)]
    
    for i in range(len(a)): 
        d[a[i]].append(i) 
    
    ans = 1
    
    pairs = [[] for _ in range(1001)]
    
    
    for i in range(1, 1001):
        for j in range(1, 1001): 
            if math.gcd(i, j) == 1:
                pairs[i].append(j)

    for i in range(1, 1001): 
        for j in pairs[i]:
            ans = max(ans, d[i][-1]+ d[j][-1] + 2)

    print(ans)

for _ in range(int(input())):
    solve()
