import math 

def help(num):
    pass
    
def solve():
    x,y,k = map(int, input().split())
    
    for i in range(0, k - k % 2):
        print(x - ((1 if i % 2 != 0 else -1) * (i//2 + 1)), y) 
        
    if k % 2 != 0:
        print(x, y)
        
    
for _ in range(int(input())):
    solve()
