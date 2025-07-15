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

    eflg = 0
    oflg = 0

    for i in range(n):
        if a[i] % 2 == 0:
            eflg = 1
        else:
            oflg = 1

        if eflg and oflg:
            print(2)
            return

    for i in range(1, 57):

        cnter = set()
        flg = 1

        for j in range(n):

            cnter.add(a[j] % (2 ** i))

            if len(cnter) > 2:
                flg = 0
                break

        if len(cnter) == 2 and flg == 1:
            print(2**i)
            return


for _ in range(int(input())):
    solve()
