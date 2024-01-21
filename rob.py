class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, noRob = 0,0 

        for num in nums: 
            newRob = noRob + num 
            newNoRob = max(noRob, rob)

            rob, noRob = newRob, newNoRob 
        
        return max(rob, noRob)
