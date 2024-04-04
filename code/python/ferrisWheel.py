n, x = map(int, input().split()) 

ans = 0  

a = list(map(int, input().split())) 

a.sort()

pt1 = 0
pt2 = n - 1

while(pt1 < pt2):
    if a[pt1] + a[pt2] <= x:
        a[pt2] += a[pt1]
        pt1 += 1
        
    else:
        pt2 -= 1
        
print(n - pt1)
    
    
    




