class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        v1, v2, ans = [], [], []

        for num in nums: 
            if num > 0: 
                v1.append(num)
            elif num < 0:
                v2.append(num)
        
        i1, i2 = 0, 0

        while i2 < len(nums) // 2:
            ans.append(v1[i1])
            i1 +=1 
            ans.append(v2[i2])
            i2 += 1

        return ans
