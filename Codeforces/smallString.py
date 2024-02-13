t=int(input()) 

def sol(n):
    for i in range(1,26):
        for j in range(1,26):
            k = n - (i+j)
            if 1 <= k <= 26:
                print(chr(i+96),chr(j+96),chr(k+96))
                    

for _ in range(t): 

    n = int(input()) 
    
    print(n,'\n')
    # n = 13
    print(sol(n))

    
       