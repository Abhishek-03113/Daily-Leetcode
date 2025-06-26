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


def diff(a, b):
    a = list(str(a))
    b = list(str(b))
    ans = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            ans += 1
    return ans


def solve():
    l, r = io()
    lol = []

    for i in range(l, r+1):
        lol.append(diff(l, i) + diff(i, r))

    print(min(lol) if lol else 0)


for _ in range(int(input())):
    solve()
