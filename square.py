t = int(input()) 
for _ in range(t): 
    
    corners = [] 
    
    for i in range(4):
        
        x, y = map(int, input().split()) 
        
        corners.append([x,y]) 
    
    side_length = 0
    
    
    for i in range(4):
        
        for j in range(i+1, 4): 
            
            dx = abs(corners[i][0] - corners[j][0])
            dy = abs(corners[i][1] - corners[i][1])
            
            side_length = max(side_length, dx, dy)

    
    area = side_length**2 
    
    print(area)