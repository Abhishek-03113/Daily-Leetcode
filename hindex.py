"""
@Abhishek 
Day 31 
Topic : array 

"""


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        citations.sort()

        for i in range(n):
            if citations[i] >= n - i:
                return n - i

        return 0
