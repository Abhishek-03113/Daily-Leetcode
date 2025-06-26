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

    flg = 0

    for i in range(1, n):
        if abs(a[i] - a[i-1]) <= 1:
            print(0)
            return
    if len(a) < 3:
        print(-1)
        return

    for i in range(0, n-2):
        l = a[i]
        r = a[i+2]
        mm = max(a[i], a[i+1])
        mn = min(a[i], a[i+1])

        mxx = max(a[i+2], a[i+1])
        mnn = min(a[i+2], a[i+1])

        if (l <= mxx and l >= mnn) or (l-1 <= mxx and l-1 >= mnn):
            print(1)
            return

        elif (r <= mm and r >= mn) or (r-1 <= mm and r-1 >= mn):
            print(1)
            return

    print(-1)


for _ in range(int(input())):
    solve()
