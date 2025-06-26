import math
import os
import sys
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from functools import lru_cache, reduce
mod = 10**9 + 7


def io():
    return map(int, input().split())


def iol():
    return list(map(int, input().split()))


def ios():
    return input().strip()


def ioi():
    return int(input().strip())


def iom(n, m):
    return [list(map(int, input().split())) for _ in range(n)]


def solve():
    a, x, y = io()

    x_dist_a = abs(x - a)
    y_dist_a = abs(y - a)

    y_x = abs(y - x) 
    
    if x_dist_a > y_x and y_dist_a > y_x:
        print("YES")
        return  

    xx = 0 
    yy = 0
    for i in range(0,100):
        if i != a: 
            xx = abs(i - x) 
            yy = abs(i - y)
            if xx < x_dist_a and yy < y_dist_a:
                print("YES")
                return 
    print("NO")

for _ in range(int(input())):
    solve()
