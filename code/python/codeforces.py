def help(s,t, x): 
    pass
import math
def solve():
    
    n = int(input()) 
    p = list(map(int, input().split()))
    
    ans = 0 
    

    mid = n // 2
    sort = True 
    for i in range(n):
        if p[i] != i + 1:
            sort = False
            break
        
    if sort:
        print(0)
        
    elif p[mid] == mid + 1:
        print(1)
    else:
        print(2)
        

    
        
    # n = int(input())
    # s = input()     s
    # win = n

    # optimal = {'R':'P', 'P':'S', 'S':'R'}
    # prev = ''
    
    # for i in range(n):    
    #     if prev == optimal[s[i]]:
    #         win -= 1
    #         prev = ''
    #     else:
    #         prev = optimal[s[i]]
            
    # print(win)

for _ in range(int(input())):
    solve()

# for _ in range(int(input())):
    
#     ans = solve() 
#     # print(*ans)