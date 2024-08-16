def solve():
    n = int(input()) 
    a = list(map(int,input().split())) 

    if n > 2:
        print("NO")
        return
    else:
        if (abs(a[0] - a[1]))> 1:
            print("YES") 
            return
    
    print("NO")

for _ in range(int(input())):
    solve() 