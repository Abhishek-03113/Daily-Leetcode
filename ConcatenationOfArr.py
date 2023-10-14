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

        for i in range(len(ans)):
            ans[i] = nums[i]
        
            ans[i+n] = num[i]
        


        return ans
