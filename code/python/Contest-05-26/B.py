def power(n):
    if n < 1:
        return 1 
    lower_power = 2 ** (n.bit_length() - 1)
    upper_power = lower_power * 2
    
    
    l = n.bit_length() - 1 
    h = n.bit_length() 
    
    if (n - lower_power) <= (upper_power - n):
        # return lower_power
        return l 
    else:
        return h 
    

for _ in range(int(input())):
    
    
    x = int(input()) 
    
    if x == 1:
        print(1)
        print(1)
        continue     

    else:        
        p = power(x) + 1 
        
        print(p)
        
        
        for i in range(0, p):
            
            print(2 ** i, end = " ") 
        
        print()
            
    