"""
@Abhishek 
Day 41 
Topic : matrix, hashmap, arrays 
"""


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        grps = defaultdict(list)

        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                diagonal = row + col
                grps[diagonal].append(nums[row][col])

        ans = []
        curr = 0

        while curr in grps:
            ans.extend(grps[curr])
            curr += 1

        return ans
