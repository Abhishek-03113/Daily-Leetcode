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
    n, q = io()
    a = iol()
    k = iol()
    pre = [0]*(n+1)
    for i in range(1, n+1):
        pre[i] = pre[i-1] + a[i-1]

    ids = [([k[i], i]) for i in range(q)]
    ids.sort() 

    ans = [0]*q
    prev = 0

    for val, id in ids:
        it = prev
        while it < n and val >= a[it]:
            it += 1
        ans[id] = pre[it]
        prev = it
    print(*ans)


for _ in range(int(input())):
    solve()
