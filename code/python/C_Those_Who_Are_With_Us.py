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
    n, m = io()
    mat = iom(n, m)
    mx = 0
    mx_ = 0
    for i in range(n):
        for j in range(m):
            mx = max(mx, mat[i][j])

    r = [0] * n
    c = [0] * m

    for i in range(n):
        for j in range(m):
            if mat[i][j] == mx:
                mx_ += 1 
                r[i] += 1
                c[j] += 1
    
    for i in range(n):
        for j in range(m): 
            if r[i] + c[j] - (int(mat[i][j] == mx)) == mx_:
                flg = 1 
                return print(mx - 1)
    
    print(mx) 


for _ in range(int(input())):
    solve()
