t=int(input()) 
def sol(n):
    ans = [1,1,1]
    
    n-= 3 
    
    if n > 0:
        diff = min(25,n)
        ans[2] += diff
        n -= diff 
    if n > 0:
        diff = min(25,n)
        ans[1] += diff
        n -= diff
    if n > 0:
        diff = min(25,n)
        ans[0] += diff
        n -= diff 
            
    ans[0] = chr(96+ans[0])
    ans[1] = chr(96+ans[1])
    ans[2] = chr(96+ans[2])
    
    return ''.join(ans)

    

for _ in range(t): 
    n = int(input()) 
    print(sol(n))

