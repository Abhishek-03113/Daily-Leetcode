class Solution:
    def reverse(self, x: int) -> int:

        if x >= (2**31) or x <= (-2**31):
            return 0 

        if x>=0:
            ans = int(str(x)[::-1]) 

            if ans >= (2**31) or ans <= (-2**31):
                return 0 
            return ans 
        
        elif x<0: 
            ans = -(int(str(abs(x))[::-1]))
            
            if ans >= (2**31) or ans <= (-2**31):
                return 0 
            return ans
