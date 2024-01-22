class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        # s : set of integers, 
        s = set() 

        ans = []

        for i in range(len(nums)):

            if nums[i] not in s:
                s.add(nums[i])
            else:
                ans.append(nums[i])
        
        for j in range(1, len(nums)+1):

            if j not in s:
                ans.append(j)

            


        return ans 


