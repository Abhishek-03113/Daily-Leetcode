def solve():
    # n = int(input()) 
    # a = list(map(int, input().split())) 
    # a.sort() 
    
    # if n % 2:
    #     return ["NO" ]
    
    # ans = [0]*n 
    
    # j = 0
    # k = n // 2
    
    # for i in range(n):
        
    #     if i % 2 == 0:
    #         ans[i] = a[j]
    #         j += 1
            
    #     else:
    #         ans[i] = a[k]
    #         k +=1     

    
    # for i in range(1, n-1): 
        
        
    #     if ans[i]>ans[i-1] and ans[i] > ans[i+1]:
    #         continue
            
    #     elif ans[i]< ans[i-1] and ans[i] < ans[i+1]:
    #         continue 
            
    #     else:
    #         return ["NO"]
    # print("YES")
    # return ans
for _ in range(int(input())):
    
    ans = solve() 
    print(*ans)
    # n = int(input())
    # s = list(input())

    # open = 0

    # for i in range(n):

    #     if s[i] == '(':
    #         open += 1

    #     if s[i] == '_' and open > 0:
    #         s[i] = ')'
    #         open -= 1
    #     elif s[i] == '_' and open == 0:
    #         s[i] = '('
    #         open += 1
    #     elif s[i] == ")":
    #         open-=1

    # stack = []

    # ans = 0

    # for i in range(n):
    #     if s[i] == '(':
    #         stack.append(i)
    #     else:
    #         ans += (i-stack.pop())
    # print(ans)
