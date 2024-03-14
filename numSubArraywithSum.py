class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        # nums = binary array 

        # goal = integer 

        # sum of subarray == integer



        count = {0:1} 

        curr = 0



        total = 0 



        for i in nums: 

            curr += i 



            if curr - goal in count:

                total += count[curr-goal] 



            count[curr] = count.get(curr, 0) + 1 

    

        return total 

        
