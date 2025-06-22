import math
import os
import sys
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce
mod = 10**9 + 7

# function overloading for input


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
    n, s = io() 
    a = iol() 
    
    min_ = min(a) 
    mx = max(a)  
    
    diff_mn = abs(min_ - s) 
    diff_ms = abs(mx - s) 
    ans = 0 
    
    if diff_mn < diff_ms: 
        ans = abs(min_ - s) + abs(mx - min_) 
    else:
        ans = abs(mx - s) + abs(min_ - mx)
    print(ans)          


for _ in range(int(input())):
    solve()
