""""
@Abhishek 
Day 4 : Problem 3


"""


class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        """
        n = len(nums)

        ans = [0] * 2*n

        for i in range(len(nums)):
            ans[i] = nums[i]
        
            ans[i+n] = nums[i]
        


        return ans

        ## Alternate Solution 
        ## return nums*2 or nums+nums 

