t = int(input()) 

for _ in range(t):
    score = 0 
    
    n = int(input()) 
    
    a = list(map(int, input().split()))
    
    a = sorted(a)
    for i in range(1, 2*n,2):
        x, y = a[i], a[i-1]
        score += min(x, y) 
        
    print(score)


    