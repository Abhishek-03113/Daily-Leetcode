# def solution(): 
t = int(input()) 

for _ in range(t):
    score = 0 
    end = 0 
    n = int(input()) 
    a = input() 

    for i in range(1, n):
        if a[i] == '@':
            score += 1 
        if a[i] == '*': 
            if a[i-1] == "*":
                end = i-1
                break 
    
    print(score) 

