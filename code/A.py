from collections import Counter 
t = int(input()) 

for _ in range(t):
    s = input() 
    c = Counter(s)
    
    a = c['A'] ; b = c['B']
    
    if a > b:
        print('A')
    else:
        print('B')