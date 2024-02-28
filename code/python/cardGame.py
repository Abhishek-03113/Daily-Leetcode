from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())

    trump = input()

    a = list(input().split()) 
    
    h = {
        'S': [],
        'H': [],
        'D': [],
        'C': []
    }

    for i in a:
        h[i[1]].append(i[0])
    
    
    for i in h:
    
        if len(h[i]) == 0:
            continue 
            
        if len(h[i]) % 2 == 0:
            for j in range(len(h[i])):
                temp = h[i].
                print(f"{i}{temp}", end=" ")
                
            print("")
    