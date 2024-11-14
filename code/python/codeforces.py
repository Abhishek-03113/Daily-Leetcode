import math
from collections import Counter

# def solve():
    
#     n, k = map(int, input().split()) 
    
#     a = list(map(int, input().split())) 
    
#     mp = {} 
    
#     for i in a: 
#         mp[i] = 1 + mp.get(i, 0) 
    
#     dist, dup = len(mp), n - len(mp)
    
   
    
#     if dup >= k: 
#         dup -= k 
#     else: 
#         dup = 0 
    
#     print(dist, dup)
#     print(math.comb(n,2) - dup)
        
# for _ in range(int(input())): 
#     solve()

def solve(n, m, r, blue_balls):
    red = {}
    for xi, ui in r:
        prod = xi * ui
        if prod in red:
            red[prod] += 1
        else:
            red[prod] = 1

    ans = 0
    for yi, vi in blue_balls:
        prod = yi * vi
        if prod in red and r[prod] > 0:
            ans += 1
            r[prod] -= 1

    return ans

n, m = map(int, input().split())
r = [tuple(map(int, input().split())) for _ in range(n)]
blue_balls = [tuple(map(int, input().split())) for _ in range(m)]

print(solve(n, m, r, blue_balls))
