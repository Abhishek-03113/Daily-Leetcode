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

    ans = 0

    amap = [(k, v) for v, k in enumerate(a)]
    amap = sorted(amap, reverse=True)

    for j in range(n):
        for k in range(j + 1, n):
            s = a[j] + a[k]

            for v, ind in amap:
                if ind != j and ind != k:
                    ans = max(ans, v % s)
                    break

    print(ans)


for _ in range(int(input())):
    solve()
