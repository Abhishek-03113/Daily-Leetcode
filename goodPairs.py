"""
@Abhishek 
Day 19 
Problem : goodPairs 

"""


class Solution:
    # Bruteforce
    # def numIdenticalPairs(self, nums: List[int]) -> int:
    #     count = 0

    #     for i in range(len(nums)):

    #         for j in range(len(nums)):

    #             if nums[i] == nums[j] and i<j:
    #                 count +=1

    #     return count

    # Optimal
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum([math.comb(n, 2) for n in collections.Counter(nums).values()])
