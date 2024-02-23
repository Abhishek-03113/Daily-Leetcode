t = int(input()) 

for _ in range(t): 
    
    n, k = map(int, input().split()) 
    a = list(map(int,input().split()))
    x = list(map(int,input().split()))
    
    z = [0] * (n+1)
    flg = True
    for i in range(n):
        z[abs(x[i])] += a[i] 
    
    power = k 
    
    for i in range(1,n+1):
        
        if power < z[i]:
            print('NO')
            flg = False
            break 
        
        power -= z[i]
        
        power += k 
    
    if flg:
        print("YES")
        
    