import math
import os
import sys
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce
mod = 10**9 + 7


def help(m, x):

    left, right = 0, len(m) - 1

    # find the first index where m[index] > x
    while left < right:
        mid = (left + right) // 2
        if m[mid] > x:
            right = mid
        else:
            left = mid + 1

    return left if m[left] > x else left + 1


def solve():
    n = int(input())
    x = list(map(int, input().split()))
    q = int(input())

    x.sort()

    for _ in range(q):
        y = int(input())
        print(help(x, y))


solve()
