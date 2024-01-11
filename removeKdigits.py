
class Solution:

    def removeKdigits(self, s, k):
        # code here
        
        stack = [] 
        
        n = len(s) 
        
        if n == k:
            return 0 
        
        stack.append(s[0])
        
        i = 1 
        
        temp = ''
        currs = ''
        
        for i in range(1, n):
            
            while (k > 0 and stack and stack[-1] > s[i]):
                stack.pop() 
                k -= 1 
            
            stack.append(s[i]) 
        
        while k:
            stack.pop() 
            k -= 1 
            
        stack = stack[::-1] 
        
        while(stack and stack[-1] == "0"):
            stack.pop()
        if not stack :
            return 0
        # print("".join([]))k76
        return "".join(stack[::-1]) 
 
