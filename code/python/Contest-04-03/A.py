from math import gcd
from functools import reduce

for _ in range(int(input())):
    
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0 
    
    min_fact = reduce(gcd, a) 
    
    if min_fact == 1: 
        print(sum(a)) 
        continue
    
    else:
        for i in a:
            ans += i//min_fact 
        
    print(ans)