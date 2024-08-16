def solve():

    n,k = map(int, input().split()) 
    a = list(map(int,input().split())) 
    
    a.sort(reverse=True) 
    
    for i in range(1,n):
        if i % 2 != 0:
            if k >= a[i-1] - a[i]:
                a[i] += a[i-1] - a[i]  
                k -= a[i-1] - a[i] 
            else:
                a[i] += k 
                k = 0 
    alice = 0
    bob = 0
    for i in range(n):
        if i % 2 == 0:
            alice += a[i] 
        else:
            bob += a[i] 
    
    print(alice - bob)

for _ in range(int(input())):
    solve()
