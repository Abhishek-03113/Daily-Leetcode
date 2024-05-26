n, k  = map(int, input().split()) 

a = list(map(int, input().split())) 

min_ = a[k-1] 

ans = 0     

for i in range(n):
    if a[i] >= min_ and a[i] > 0:
        ans += 1 
        
        
print(ans)   
