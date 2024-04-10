for _ in range(int(input())): 
    
    n, c, d= map(int, input().split())   
    
    a = list(map(int, input().split())) 
    
    
    a.sort()  
    
    b = [0] * (n * n) 
    
    b[0] = a[0]
    
    for i in range(1, n): 
        b[i] = b[i-1] + c 
        
    
    for i in range(1, n): 
        for j in range(n): 
            b[i * n + j] = b[(i-1) * n + j] + d
            
    b.sort()
    
    print("YES" if a == b else "NO")