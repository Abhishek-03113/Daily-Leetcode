for _ in range(int(input())):
    n = int(input()) 
    a = list(map(int, input().split()))
    
    new  = [a[n-1]] 
    
    for i in range(n-2, -1, -1):
        
        if a[i] > new[-1]:
            new.append(a[i]%10)
            new.append(a[i]//10)
        else:
            new.append(a[i])
        
    if new == sorted(new, reverse = True):
        print("YES")
    else:
        print("NO")

            
    