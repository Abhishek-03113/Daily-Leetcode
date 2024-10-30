def upper_bound(a, x): 
    l = 0 
    r = len(a) 
    while l < r: 
        m = (l + r) // 2 
        if a[m] <= x: 
            l = m + 1 
        else: 
            r = m 
            
    if l - 1 < 0: 
        return -1
    return l   


def solve():
    n, m = map(int, input().split()) 
    
    a = list(map(int, input().split())) 
    b = list(map(int, input().split()))  
    
    a.sort()
    
    for i in range(m): 
        ans = (upper_bound(a, b[i]))  
        
        if ans <= 0: 
            print(-1) 
        else: 
            if ans > 0:
                print(a[ans - 1])
                a[ans - 1] = float('inf')
            

        
solve() 

# for _ in range(int(input())):solve()    