n = int(input()) 


flg = False
for i in range(1, n+1):
    
    tn = (i * (i + 1)) // 2 
    
    if tn == n: 
        flg = True
        break
    
if flg:
    print('YES')
else:
    print("NO")
    