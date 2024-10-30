def solve():
    y, x = map(int, input().split()) 
    
    n = max(y, x) * (max(y, x) - 1) + 1
    
    if max(x, y)%2 == 0:
        n += y-x 
    else:
        n += x- y 
    
    print(n)
     

for _ in range(int(input())):solve()    