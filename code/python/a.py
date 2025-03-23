for _  in range(int(input())): 
    
    x,y,a = map(int,input().split()) 
    a = a + 0.5
    depth = 0 
    turn = 0
    while depth < a: 
        
        if turn == 0: 
            depth += x
            if depth >= a: 
                print('NO')
                break 
        else: 
            depth += y
            if depth >= a: 
                print('YES')
                break
        turn = 1 - turn
    
