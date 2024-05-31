for _ in range(int(input())):
    n = int(input())    
    flg = 1
    
    s = input() 
    
    if ord(s[0]) > ord(s[-1]):
        print("NO")
        continue

    for i in range(1, len(s)):
        
        # print(ord(s[i]),s)
        if ord(s[i]) < ord(s[i-1]):
            flg = 0 
            print("NO")
            break
            
       
    if flg == 1:
        print("YES") 
        
        
    
