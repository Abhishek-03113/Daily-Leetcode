for _ in range(int(input())):
    n = int(input()) 
    a = list(map(int, input().split())) 
    x = 0 
    while (a[x] != 1):
        x += 1
    y = n-1 
    while a[y] != 1:
        y -= 1
    ops = 0
    for i in range(x,y+1):
        ops += (a[i] == 0) 
    print(ops)
        
        
