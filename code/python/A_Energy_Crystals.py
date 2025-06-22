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
    x = int(input())
    a = [x for _ in range(3)]

    ans = 0

    while a !=[0,0,0]:
        a.sort()
        a[-1] = a[-2] // 2
        ans += 1

    print(ans)


for _ in range(int(input())):
    solve()
