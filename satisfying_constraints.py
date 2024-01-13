t = int(input()) 
t = 1 
for _ in range(t): 
    n = int(input()) 
    c = 0 
    c1= []
    c2 = []
    c3 = []
    for i in range(n):
        a, n = map(int, input().split()) 
        if a == 1: 
            c1.append(n)
        if a == 2: 
            c2.append(n)
        if a == 3:
            c3.append(n)
    c_1 = max(c1) 
    c_2 = min(c2) 

    c += len(range(c_1, c_2+1))

    for i in c3:
        if i in range(c_1, c_2+1    ):
            c -= 1

    print(c)