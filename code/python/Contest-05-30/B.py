for _ in range(int(input())):
    
    n = int(input()) 
    
    a = list(map(int, input().split())) 
    b = list(map(int, input().split())) 
    
    ans = [0] * (n+1) 
    
    min_ = 1e9

    for i in range(0,n):
        # ans[i] = abs(b[i] - a[i])
        min_ = min(min_, abs(b[n]-a[i]))
        min_ = min(min_, abs(b[n]-b[i])) 
        
        if (min(a[i], b[i]) <= b[n]) and (b[n] <= max(a[i], b[i])):
            min_ = 0    

    
    for i in range(n):        
        min_ += abs(a[i] - b[i])
        
    
    print(min_ + 1)