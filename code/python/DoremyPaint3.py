from collections import defaultdict

for _ in range(int(input())):
    
    n = int(input()) 
    a = list(map(int, input().split()))
    h = {}
    
    for i in a:
        h[i] = 1 + h.get(i, 0)
    
    if len(h) >= 3:
        print("NO") 
        continue 
    
    else:
        if abs( h[list(h.keys())[-1]] - h[list(h.keys())[0]]) <= 1:
            print("YES")
        else:
            print("NO")
