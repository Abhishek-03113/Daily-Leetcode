# for _ in range(int(input())):
    
n = int(input())

ans = 0
for _ in range(n):
    
    op = input() 
    
    if '+' in op:
        ans += 1 
    else:
        ans -= 1 
    
print(ans)
    
    
    