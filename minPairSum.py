class Solution:
    def minPairSum(self, nums: List[int]) -> int:   
        n = len(nums) 
        nums.sort()
        maxSum = 0
        
        for i in range(int(n/2)):
            maxSum = max(maxSum, nums[i] + nums[n-1-i])
        return maxSum