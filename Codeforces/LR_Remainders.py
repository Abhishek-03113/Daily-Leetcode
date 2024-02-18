import math 
t = int(input()) 

for _ in range(t): 
    n, m = map(int, input().split()) 
    a = list(map(int, input().split())) 
    s = input() 
    
    prod = 1
    for i in range(n):
        prod *= a[i]
    rem = prod % m 
    print(rem, end =" ")
    
    for i in s: 
        if i == 'L':
            p = a.pop(0)
            prod =  int(prod / p)   # o(n*n) 
            rem = prod % m 
            if len(a)==0:
                break
            print(rem , end= " ")
        elif i == 'R':
            p = a.pop(-1)
            prod = int(prod / p)  # o(n*n)
            rem = prod % m 
            
            if len(a)==0:
                break
            print(rem, end =" ")
    print("") 