 
I = lambda: map(int, input().strip().split())
L = lambda: list(map(int, input().split()))


def solve():
    n = int(input()) 
    a = L() 
    
    visited = set() 
    
    ans = 0 
    curr = 0
    
    
    for i in range(len(a)): 
        if a[i] not in visited: 
            curr += 1 
            visited.add(a[i]) 
        else: 
            curr = max(curr, 1)
    
        print(visited, " ", curr, " ", ans)
        ans = max(ans, curr) 

    print(ans)
            
    
        
        
        
        
        
solve() 

# for _ in range(int(input())):
#     solve() 

