import math 

def help():
    pass
    

def solve():
    # pass
    n = int(input())
    a = list(map(int, input().split())) 
    s = list(input())
   
    # print(a,s)
    
    score  = 0 
    
    l = 0 
    r = n-1
    
    while l < r:
        if s[l] == "L" and s[r] == "R":
            
            score += sum(a[l:r+1])
            l += 1
            r -= 1
        
        elif a[l] != "L":
            l += 1 
        elif a[r] != "R":
            r -= 1 
        
    print(score)    
    
    
        
        
        
        

    
for _ in range(int(input())):
    solve()
