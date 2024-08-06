def help(): 
    pass

import math

def solve():
    
    n = int(input())
    a = list(map(int, input().split()))
    
    
    mid = n // 2 
    
    l = 0
    r = 0
    
    
    for i in range(0, mid):
        
        if a[i] > a[mid]:
            l += 1
            break
        else:
            continue 
    
    for i in range(mid+1, n-1):
        if a[i] < a[mid]:
            r += 1 
            break
        else:
            continue 
    
    
    sorted_ = 1         
    
    for i in range(1,n):
        if a[i] < a[i - 1]:
            sorted_ = 0 
            break 
    
    # print(a)
    if sorted_:
        print(0)
        return

    if l == 0 and r == 0:
        print(1)
        return
    elif l and r:
        print(3)
        return
    elif l or r:
        print(2)
        return  
    
        
        
    
    # odd = sum(1 for x in a if x % 2 != 0)
    # even = n - odd     
    # if even == n or odd == n:
    #     print(0)
    #     return 
    
    # # a.sort() 
    
    # max_even = 0 
    # max_odd = 0
    # ans  = 0
    
    # v = []
    
    # for i in range(n):
    #     if a[i] % 2 == 0:
    #         v.append(a[i])
    #     else:
    #         max_odd = max(a[i], max_odd)
        
    # ans = even 
    
    # v.sort() 
    
    # for i in v:        
    #     if i < max_odd:
    #         max_odd += i 
    #     else:
    #         ans += 1
    #         break
    
    # print(ans)


                
            
        
        
    
    
    
for _ in range(int(input())):
    solve()

# for _ in range(int(input())):
    
#     ans = solve() 
#     # print(*ans)