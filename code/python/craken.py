from collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = deque(list(map(int, input().split()))) 
    sunk = 0
    
    while len(a) > 1 and k > 0:
        
        m = min(a[0], a[-1]) 
        
        if k < 2*m:
            
            a[0] -= k//2 + k%2 
            a[-1] -= k//2 
            
            k = 0 
        else:
            a[0] -= m 
            a[-1] -= m 
            k -= 2*m 
        
    
        if a[0] == 0:
            a.popleft()
        
        if a[-1] == 0:
            a.pop()
        
    sunk = (n - len(a)) + (len(a) and a[0] <= k)
    
    print(sunk)
    
                    

    
    # while k > 0 and len(a) > 0:
    #     if a[0] > 0:
    #         a[0] -= 1
    #         if a[0] == 0:
    #             a.pop(0)
    #             sunk += 1
    #     k -= 1
    #     if k > 0 and len(a) > 1 and a[-1] > 0:
    #         a[-1] -= 1
    #         if a[-1] == 0:
    #             a.pop()
    #             sunk += 1
    #         k -= 1
