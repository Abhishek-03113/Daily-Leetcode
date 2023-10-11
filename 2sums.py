""" 
@Abhishek 
Date:11-oct-2023

num = arr[int]
target = int
appraoch = bruteforce(self)
checked Solution for optimized code 

"""


class Solution(object):
    # Bruteforce
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums.sort()
        i,j = 0,0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)): 
                if nums[i]+nums[j] ==target: 
                    return i,j
        
        # return i,j

        # # Optimized 
        def OptimizedSolution(self,nums,target):
            numToIndex = {}
            for i in range(len(nums)):
                if target - nums[i] in numToIndex:
                    return [numToIndex[target - nums[i]], i]
                numToIndex[nums[i]] = i
            return []

        """
        Optimization Startergy: 
        inititated a dictionary 
        if the target-index is in dictionary return it 
        else add the item to dictionary 

        """






        
