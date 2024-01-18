s = input() 

longestRepition = 1
streak = 1

for i in range(1, len(s)):
    if s[i] != s[i-1]: 
        streak = 1
    else:
        streak += 1 
    longestRepition = max(streak, longestRepition)
        
    
print(longestRepition)