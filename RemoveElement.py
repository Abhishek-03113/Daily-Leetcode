"""
@Abhishek 
Day 21 
Topic : arrays

"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1

        return count

        # one liner list comprehension
        nums[:] = [num for num in nums if num != val]

        return len(nums)
