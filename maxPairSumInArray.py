"""
@Abhishek 
Day 19 
Topic : Hashmaps 
"""


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        ans = 0

        for each in nums:
            max_digit = int(max(str(each)))
            d[max_digit].append(each)

        for each in d:
            if len(d[each]) > 1:
                d[each].sort()
                ans = max(ans, d[each][-1] + d[each][-2])

        return -1 if ans == 0 else ans
