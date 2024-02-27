t = int(input())

for _ in range(t):
    n = int(input()) 
    a = list(map(int,input().split()))
    flg = 1
    sum_ = sum(a) 
    
    if sum_ % 3 == 0:
        print(0)
        continue 
    if sum_ % 3 == 2:
        print(1)
        continue
    for i in range(n):
        temp = sum_ - a[i]
        if temp % 3 == 0:
            print(1)
            flg = 0 
            break
    if flg:
        print(2)