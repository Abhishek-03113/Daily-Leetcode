class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        major = max(count.values())

        for i in count:
            if count[i] == major:
                return i
