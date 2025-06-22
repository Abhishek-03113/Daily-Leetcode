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
    b = iol()

    miss_a = 0
    miss_b = 0
    miss_ab = 0

    if a[0] > b[0]:
        miss_ab += 1

    for i in range(1, n):
        if a[i] < a[i-1]:
            miss_a += 1

        if b[i] < b[i-1]:
            miss_b += 1

        if a[i] > b[i]:
            miss_ab += 1

    if miss_a == miss_b == miss_ab == 0:
        print(0)
        return
    moves = 0
    move = []
    if miss_a > 0:

        for i in range(n):
            flg = False

            for j in range(0, n-i-1):
                if a[j] > a[j+1]:
                    miss_a -= 1
                    a[j], a[j+1] = a[j+1], a[j]
                    moves += 1

                    move.append([1, j+1])
                    flg = True
            if not flg:
                break

    if miss_b > 0:

        for i in range(n):
            flg = False

            for j in range(0, n-i-1):
                if b[j] > b[j+1]:
                    miss_b -= 1
                    b[j], b[j+1] = b[j+1], b[j]
                    moves += 1
                    move.append([2, j+1])
                    flg = True
            if not flg:
                break

    if miss_ab > 0:

        for i in range(n):

            if a[i] > b[i]:
                miss_ab -= 1
                moves += 1
                move.append([3, i+1])
                a[i], b[i] = b[i], a[i]

    print(moves)
    for i in move:
        print(*i)


for _ in range(int(input())):
    solve()
