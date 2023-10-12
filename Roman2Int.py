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
        special = {"IX":9,"IV":4,"XL":40,"XC":90,"CD":400,"CM":900}
        
        #Length of the string and the Integer value 
        n = len(s)
        sol = 0

        #Loop for the solution 
        if n%2!=0: 
            for i in range(0,n,2):
                if i!=n-1:
                    j = i+1
                    
                print(val[s[i]],val[s[j]])


test = Solution()

s = input("ENTER THE TEST STRING")

test.romanToInt(s)


