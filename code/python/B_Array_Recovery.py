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
    d = iol() 

    a = [0]*n 
    
    a[0] = d[0] 
    
    for i in range(1, n):
        if (a[i-1] - d[i]) >= 0 and d[i] != 0:
            print(-1)
            return
        a[i] = d[i] + a[i-1] 
    print(*a)
    
for _ in range(int(input())):
    solve()
