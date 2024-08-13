import math 

def help(num):
    pass
    
def solve():
    
    n = int(input())    
    a = list(map(int,input().split())) 
    
    m = int(input()) 
    
    s = [] 
    
    for i in range(m):
        s.append(input())
    
    # open = set()
    
    # for i, seat in enumerate(a):
        
    #     if i == 0:
    #         open.add(seat)
    #         continue 
            
    #     if not open:
    #         print("NO")

    #     if seat - 1 not in open and seat + 1 not in open and open:
    #         print("NO")
    #         return

    #     open.add(seat) 
        
    
    # print("YES")
        


    
    
    
    # a = str(int(input())) 
    
    # if not a.startswith('10') or len(a) < 3:
    #     print("NO")
    #     return 

    # exp = a[2:] 
    
    
    # if exp.startswith("0"):
    #     print("NO")
    #     return
    
    # if exp.isdigit() and int(exp) >= 2:
    #     print("YES")
    #     return
    # else:
    #     print("NO")
    #     return
    
    
    
    
    
for _ in range(int(input())):
    solve()
