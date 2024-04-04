def binary(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


n,m,k = map(int,input().split())     

a = list(map(int,input().split())) 
b = list(map(int,input().split())) 

a.sort() 
b.sort() 

ans = 0 

i, j = 0, 0

while i < n and j < m: 
    if abs(a[i] - b[j]) <= k: 
        ans += 1 
        i += 1 
        j += 1 
    elif a[i] < b[j]: 
        i += 1 
    else: 
        j += 1
    

print(ans)