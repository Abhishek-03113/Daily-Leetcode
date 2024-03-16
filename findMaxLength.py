class Solution:
    def findMaxLength(self, nums: List[int]) -> int: 

        mp = {} 

        sum_ = 0 
        max_ = 0 

        for i, num in enumerate(nums): 

            sum_ += 1 if num == 1 else - 1

            if sum_ == 0:
                max_ = i + 1
            elif sum_ in mp:
                max_ = max(max_, i-mp[sum_]) 
            
            else:
                mp[sum_] = i 

        return max_
