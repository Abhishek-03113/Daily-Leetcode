x = int(2*1e5) + 10 
ans = 0
store = [0] * x
p = [1, 10, 100, 1000, 10000, 100000, 100000, 1000000]
for i in range(1,x):
    if i > 9:
        ct = 0 
        temp = i 
        
        for j in range(1,8):
            l = temp % p[j]
            temp -= l 
            l //= p[j-1]
            ct += l 
        ans += ct 
    else:
        ans += i 
    
    store[i] = ans

for _ in range(int(input())):
    
    n = int(input()) 
    print(store[n])