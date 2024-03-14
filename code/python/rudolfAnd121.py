for _ in range(int(input())): 
    
    n = int(input()) 
    a = list(map(int, input().split())) 
    
    for i in range(1, n-1): 
        if a[i-1] != 0:
            while a[i-1] != 0 and a[i] > -1: 
                a[i-1] -= 1 
                a[i] -= 2 
                a[i+1] -= 1 
        else:
            continue 
    print(a) 