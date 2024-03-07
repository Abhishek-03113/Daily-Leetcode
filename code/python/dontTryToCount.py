for i in range(int(input())):
    
    n, m = map(int, input().split())
    
    x = input()
    s = input() 
    
    flag = False
    
    for i in range(6):
        
        if s not in x:
            x = x + x 
        else:
            print(i)
            flag = True
            break 
    if not flag:
        print(-1)
    
    