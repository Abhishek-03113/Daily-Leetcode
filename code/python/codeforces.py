import math
from collections import Counter

def solve(n, m, r, b):
    red = {}
    for xi, ui in r:
        prod = xi * ui
        if prod in red:
            red[prod] += 1
        else:
            red[prod] = 1

    ans = 0
    for yi, vi in b:
        prod = yi * vi
        if prod in red and red[prod] > 0:
            ans += 1
            red[prod] -= 1  

    return ans

n, m = map(int, input().split())
r = [tuple(map(int, input().split())) for _ in range(n)]
b = [tuple(map(int, input().split())) for _ in range(m)]

print(solve(n, m, r, b))
