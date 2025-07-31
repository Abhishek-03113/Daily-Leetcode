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
    n = int(input())
    p = list(map(int, input().split()))
    dq = deque(p)
    q = []

    i = 0
    while dq:
        if len(dq) == 1:
            dq.popleft()
            q.append('L')
            break
            
        left = dq[0]
        right = dq[-1]

        if i % 2 == 0:
            if left < right:
                dq.popleft()
                q.append('L')
            else:
                dq.pop()
                q.append('R')
        else:
            if left > right:
                dq.popleft()
                q.append('L')
            else:
                dq.pop()
                q.append('R')
        
        i += 1

    return ''.join(q)


t = int(input())
for _ in range(t):
    print(solve())
