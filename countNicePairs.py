"""
@Abhishek Day 40 
Topic Hashmap, array 
"""


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        def rev(x):
            return int(str(x)[::-1])
        ans = 0  
        arr = [] 
        for i in range(len(nums)):

            arr.append(nums[i] - rev(nums[i]))
        dic = defaultdict(int)
        MOD = 10 ** 9 + 7 
        for num in arr: 
            ans = (ans+dic[num]) % MOD
            dic[num] += 1 


    
        return ans