for _ in range(int(input())):
    n = int(input())
    
    l = list(map(int,input().split()))
    
    d = dict()
    for i in l:
        if i not in d:
            d[i] = 0
        d[i] += 1
    
    ans = 1
    pt = 0
    for i in range(n // 2):
        if i in d: 
            if n - i - 1 in d:
                # if one say he is start and one say he is at end
                if d[i] + d[n - i - 1] == 2:
                    ans *= 2
                else:
                    pt = 1
            # dono bolre ki dono samne the
            elif d[i] == 2:
                ans *= 2
            else:
                pt = 1
        #dono bolre last hai the ham
        elif n - i - 1 in d:
            if d[n - i - 1] == 2:
                ans *= 2
            else:
                pt = 1
        
        else:
            pt = 1
            
    
    # middle people
    if pt == 0 and n % 2 == 1:
        if n // 2 in d:
            if d[n // 2] != 1:
                
                pt = 1
            
            
        else:
            pt = 1
    
    
    if pt == 1:
        print(0)
    else:
        print(ans % 998244353)