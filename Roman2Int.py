"""
@Abhishek 
Day 2 
Convert the Roman String to integer
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Roman numerals are usually written largest to smallest from left to right

"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary Containing the value map of roman to integer
        val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sol = 0
        for i in range(len(s)):
            if i<len(s)-1 and val[s[i]] < val[s[i+1]]:
                sol -=val[s[i]]
            else:
                sol += val[s[i]]
        
        
        
        return sol

## 

test = Solution()
s = input("Enter The Roman Number ")
answer = test.romanToInt(s)

print(f"Interger Value of the Roman Number is {answer}")


