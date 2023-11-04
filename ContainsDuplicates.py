"""
@Abhishek 
Day 23 
Topic Arrays, hashmaps hash 
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)

        """using sets """
        # if len(nums) == len(nums_set):
        #     return False
        # else:
        #     return True

        """SORTING """
        # count = 1
        # nums.sort()
        # for i in range(1,len(nums)):

        #     if nums[i] == nums[i-1]:

        #         count += 1

        #     if count >= 2:
        #         return True
        # return False

        """Using Hashmaps"""

        # store = dict()

        # for i in range(len(nums)):

        #     if nums[i] not in store:
        #         store[nums[i]] = 1
        #     else:
        #         store[nums[i]] += 1

        #         return True

        # return False

        """using the set"""

        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False
