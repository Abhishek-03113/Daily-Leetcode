for _ in range(int(input())):
    
    n = int(input()) 
    
    a = list(map(int,input().split()))
    
    a = sorted(a) 
    
    i = a.pop(0) 
    j = a.pop(-1) 
    k = a.pop(0) 
    l = a.pop(-1) 
    
    print(abs(i-j) + abs(j-k) + abs(k-l) + abs(l-i))  
    
        
        