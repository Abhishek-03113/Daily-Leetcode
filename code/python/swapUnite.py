for _ in range(int(input())):
    
    s = input() 
    h = {}
    
    for i, j in enumerate(s):
        if j not in h:
            h[j] = [i]
        else:
            h[j].append(i)
            
    
    ans = float('inf')
    
    min_index =  float('inf')
    
    for i in h:
        if len(h[i]) < min_index:
            min_index = len(h[i])
    
    print(min_index)
    
    for key, val in h.items():
        ind = len(val)

        if ind == min_index:
            ops = sum((val[j] - val[j-1]-1 )for j in range(1, ind))
            ans = min(ans, ops)
        else:
            continue 
    print(ans)
    