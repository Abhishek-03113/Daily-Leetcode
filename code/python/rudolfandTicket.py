for _ in range(int(input())):
    n,m,k = map(int, input().split())
    
    left = list(map(int, input().split())) 
    right = list(map(int, input().split())) 
    right.sort() 
    left.sort() 
    
    ans = 0
    for i in range(n):
        for j in range(m): 
            if left[i] + right[j] <= k:
                ans += 1 
    
    print(ans)