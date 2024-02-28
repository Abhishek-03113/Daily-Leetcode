for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    
    # shift 
    ans = 0 
    k = a[0]
    
    for i in range(0, n-1):
        
        a[i] = a[i+1]
         
    a[n-1] = k   
    
    for i in range(0,n-1):
        
        ans += a[i] + a[i+1]
    print(ans)