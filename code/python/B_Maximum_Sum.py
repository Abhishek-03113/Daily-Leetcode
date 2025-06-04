import math
import os
import sys
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce


def solve():
    n, k = map(int, input().split())

    a = list(map(int, input().split()))

    a.sort()

    pre = [0] * (n + 1)

    for i in range(n):
        pre[i + 1] = pre[i] + a[i]

    ans =0 
    
    for i in range(k + 1):
        ans = max(ans, pre[n-(k-i)] - pre[2*i]) 

    print(ans)

for _ in range(int(input())):
    solve()
