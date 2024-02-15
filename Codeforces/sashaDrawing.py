import math 
t = int(input()) 

for _ in range(t):
    n,  k = map(int, input().split()) 
    diagonal = 4*n - 2
    
    if k == diagonal:
        cells = math.ceil(k/2) + 1
    else:
        cells = math.ceil(k/2)
    print(cells)