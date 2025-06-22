import math
import os
import sys
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce
mod = 10**9 + 7


def solve():
    n = int(input())

    print(2*n-1)
    print(1, 1, n)

    for i in range(2, n+1):
        print(i, 1, i - 1)
        print(i, i, n)


for _ in range(int(input())):
    solve()
