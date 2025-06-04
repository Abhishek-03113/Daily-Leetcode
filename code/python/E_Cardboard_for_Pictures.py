import math
import os
import sys
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce


def square(s, w):

    area = 0

    for i in range(len(s)):
        area += ((s[i] + 2*w)**2)
    return area


def solve():
    n, c = map(int, input().split())
    s = list(map(int, input().split()))

    limit = 10**9
    low = 1

    while low < limit:
        mid = (low + limit) // 2

        if square(s, mid) == c:
            print(int(mid))
            return
        elif square(s, mid) < c:
            low = mid + 1
        else:
            limit = mid
    print(int(low))


for _ in range(int(input())):
    solve()
