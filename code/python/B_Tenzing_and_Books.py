import math
import os
import sys
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce


def solve():
    n, x = map(int, input().split())

    pre = [[] for _ in range(3)]

    arrs = [list(map(int, input().split())) for _ in range(3)]

    for i in range(3):
        s = 0
        pre[i].append(s)
        for a in arrs[i]:
            if (s | a) != s:
                s |= a
                pre[i].append(s)

    ans = 0

    for i in pre[0]:
        for j in pre[1]:
            for k in pre[2]:
                if (i | j | k) == x:
                    ans = 1
                    

    if ans:
        print("Yes")
    else:
        print("No")


for _ in range(int(input())):
    solve()
