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
    n, c = io()
    a = iol()

    cpy = a[:]
    ans = 0

    while cpy:

        ind = -1
        curr = 2

        for i in range(len(cpy)):
            temp = 1 if cpy[i] > c else 0
            if temp < curr or (temp == curr and cpy[i] > cpy[ind]):
                curr = temp
                ind = i

        ans += curr
        cpy.pop(ind)

        for i in range(len(cpy)):
            cpy[i] *= 2

    print(ans)


for _ in range(int(input())):
    solve()
