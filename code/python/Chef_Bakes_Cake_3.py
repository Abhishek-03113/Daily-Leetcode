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

    ans = float('-inf')

    ans = max(ans, 0)

    for x in set(a):
        curr = 0
        for i in a:
            s = min(x, i)
            pf = s * 50 - x * 30
            curr += pf

        ans = max(ans, curr)

    print(ans)


for _ in range(int(input())):
    solve()
