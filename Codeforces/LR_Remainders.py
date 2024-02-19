import math 

t = int(input()) 

for _ in range(t): 
    n, m = map(int, input().split()) 
    a = list(map(int, input().split())) 
    s = input() 
    ans = []
    prod = 1
    for i in range(n):
        prod *= a[i]
    rem = prod % m 
    ans.append(rem)
    # print(rem, end =" ")
    
    l, r = 0, n-1 
    i = 0
    while l < r:
        
        if s[i] == 'L':
            prod = prod // a[l] 
            rem = prod % m 
            ans.append(rem)
            # print(rem, end=" ")
            l += 1
        else:
            prod = prod // a[r] 
            rem = prod % m 
            # print(rem, end=" ")
            ans.append(rem)
            r -= 1 
        
        i += 1
        
    print(' '.join(map(str, ans)))
