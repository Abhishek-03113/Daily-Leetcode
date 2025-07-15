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

    ans = float('inf')

    ans = min(ans, a[n-1])

    ans = min(ans, a[0])

    suff = [float('inf')] * (n + 1)
    for j in range(1, n + 1):
        suff[j] = a[j-1]

    for j in range(n, 0, -1):
        if j < n:
            suff[j] = min(suff[j], suff[j+1])

    for i in range(1, n + 1):
        pre = a[i-1]

        if i < n:

            ans = min(ans, pre + suff[i+1])
        else:

            ans = min(ans, pre)

    print(ans)


for _ in range(int(input())):
    solve()
