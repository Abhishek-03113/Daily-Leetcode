"""
@Abhishek
Day 30 
Topic Array 
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        next = 0

        current = 0
        i = 0
        n = len(nums)

        for i in range(0, n - 1):
            next = max(next, i + nums[i])

            if current == i:
                steps += 1
                current = next

        return steps
