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
    s = list(map(int, input().split()))

    mp = Counter(s)
    ans = 0

    ans += mp[4]

    ans += mp[3]
    mp[1] = max(0, mp[1] - mp[3])

    ans += (mp[2] + 1) // 2
    if mp[2] % 2 == 1:
        mp[1] = max(0, mp[1] - 2)

    ans += (mp[1] + 3) // 4

    print(ans)


solve()
