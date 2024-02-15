t = int(input()) 

for _ in range(t):
    s = "" 
    a,b,c = 0,0,0 
    for i in range(3):
        s += input() 
        

    for i in s:
        
        if i == "A":
            a+= 1 
        elif i == 'B':
            b += 1
        elif i == "C":
            c +=1 

    if a != 3 :
        print('A')
    elif b != 3:
        print('B')
    else:
        print('C')