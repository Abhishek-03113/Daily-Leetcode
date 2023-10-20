"""
@Abhishek 
Day 3 

This one is easy 
Solved with converting it to string and reversing the string 
Time to try without converting it to string 

"""



class Solution(object):

    # Converting it to String

    # def isPalindrome(self, x):
    #     """
    #     :type x: int
    #     :rtype: bool
    #     """
    #     rev = str(x)[::-1]

    #     if str(x) == rev: 
    #         return True
    #     else: 
    #         return False

    # Without Converting it to string
    
    def isPalindrome(self,x):
        ver = x
        rev = 0 
        dig = 0 
        if x<0:
            return False

        while (x!=0):

            dig = x %10 
            rev = rev*10 + dig
            x = x//10
        return rev == ver


x = int(input())
test = Solution()

print(test.isPalindrome(x))


