for _ in range(int(input())):
    
    p1, p2, p3 = map(int, input().split()) 
    
    if (p1+p2+p3) % 2 != 0:
        print(-1)
    else:
        print(min(((p1+p2+p3)//2), (p1+p2)))