class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort() 

        n = len(nums)

        dp = [1] *  n 

        max_size , max_ind = 1, 0 

        for i in range(1, n):
            for j in range(i):

                if nums[i] % nums[j] == 0:

                    dp[i] = max(dp[i],dp[j]+1)

                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_ind = i 

        res = []

        num = nums[max_ind]

        for i in range(max_ind, -1, -1): 

            if num % nums[i] == 0 and dp[i] == max_size:
                res.append(nums[i])
                num = nums[i] 
                max_size -= 1 
        
        return res


