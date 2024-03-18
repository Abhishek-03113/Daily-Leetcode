def is_sorted(arr):
    return arr == sorted(arr, reverse=True)

for _ in range(int(input())):
    n = int(input()) 
    a = list(map(int, input().split()))
    
    new  = [a[n-1]] 
    
    if is_sorted(a):
        print("YES") 
        continue 
    
    for i in range(n-2, -1, -1):
        
        if a[i] > new[-1]:
            new.append(a[i]%10)
            new.append(a[i]//10)
        else:
            new.append(a[i])
        
    if is_sorted(new):
        print("YES")
    else:
        print("NO")

            
    