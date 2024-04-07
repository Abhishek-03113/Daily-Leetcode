import math 
n, d = list(map(int, input().split())) 
a = list(map(int, input().split())) 

a.sort(reverse=True) 

ans = 0 

temp = n 

for i in a:
    x = math.floor(d/i) + 1 
    if x <= temp: 
        ans += 1 
        temp = temp - x 
 
print(ans)
# l, r = 0 , n-1 

# ans = 0 

# while l < r:
    
#     if a[l] * (n - r)> d:
#         ans += 1
#         l += 1 
#         r -= 1 
#     else: 
#         r -= 1     
    
# print(ans) 
