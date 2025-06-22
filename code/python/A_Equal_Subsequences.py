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
    n, k = map(int, input().split()) 
    
    if n == k: 
        print('1'*n) 
    
    else: 
        print(k * '1' + (n - k) * '0') 

for _ in range(int(input())):
    solve()
