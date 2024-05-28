for _ in range(int(input())):
    
    n, m = map(int, input().split()) 
    
    if n < m:
        print("NO") 
    elif n > m:
        if (n-m)%2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
