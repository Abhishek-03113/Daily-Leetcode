import math
import os
import sys
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce
mod = 10**9 + 7


def f(a, x):
    return [a[i] % x for i in range(len(a))]


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ans = mod
    fwd = f(a, ans)
    bwd = fwd[::-1]
    if fwd == bwd:
        print(ans)
        return
    
    print(ans)


for _ in range(int(input())):
    solve()
