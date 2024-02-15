t = int(input()) 

for _ in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    a.sort()
    ans = []
    for i in range(1,n):
        b = a[i] - a[i-1]
        ans.append((b))
        
    print(sum(ans))
        