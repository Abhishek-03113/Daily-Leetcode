import math
import os
import sys
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce


def dist(a, b):
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]))


def solve():
    n, k, a, b = map(int, input().split())
    cts = list()
    for _ in range(n):
        x, y = map(int, input().split())
        cts.append((x, y))

    dist_between_a_b = dist(cts[a - 1], cts[b - 1])

    # closest major city from b

    min_major = float('inf')

    for i in range(0, k):
        if dist(cts[b - 1], cts[i]) < min_major:
            min_major = min(min_major, dist(cts[b - 1], cts[i]))

    # closest major city from a
    min_major_a = float('inf')

    for i in range(0, k):
        if dist(cts[a - 1], cts[i]) < min_major_a:
            min_major_a = min(min_major_a, dist(cts[a - 1], cts[i]))

    print(min(dist_between_a_b, min_major + min_major_a))


for _ in range(int(input())):
    solve()
