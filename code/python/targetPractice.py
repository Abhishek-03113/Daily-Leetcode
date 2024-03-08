for _ in range(int(input())):
    
    
    n = 10 
    s = []
    score = 0
    
    for i in range(10):
        s.append(input())
        
    row = len(s)
    column = len(s[0])
    
    for i in range(row):
        for j in range(column):
            
            if i < 5:
                if s[i][j] == "X":
                    score += (i + 1)
            else:
                if s[i][j] == "X":
                    score += (i-6)
                
    print(score)