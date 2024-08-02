for _ in range(int(input())): 
    
    
    n = int(input()) 
    
    ip = [input() for _ in range(2)] 
    ans = 0
    
    
    for i in range(n):
        
        if ip[0][i] == '.' and ip[1][i] == '.': 
            reach = (i > 0 and ip[0][i-1] == '.') or (i < n-1 and ip[0][i+1] == '.')
            reach1 = (i > 0 and ip[1][i-1] == '.') or (i < n-1 and ip[1][i+1]=='.')
            
        
            if reach and reach1:
                ans += 1 
            
    print(ans)