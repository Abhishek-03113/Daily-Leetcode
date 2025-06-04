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
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort(reverse=True)
    a.sort()

    ans = 1

    for i in range(n):
        cnt = len(a) - bisect_right(a, b[i]) 
        ans = ans * max(cnt - i, 0) % mod
    print(ans) 
for _ in range(int(input())):
    solve()
