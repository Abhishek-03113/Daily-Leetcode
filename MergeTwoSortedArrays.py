#!/usr/bin/python3

"""
@Abhishek 
Day 19 
Topic : Two Pointers, Array, Sorting 

"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1.append((0) * n)

        return nums1


test = Solution()


nums1 = [1, 2, 3, 4, 5]
nums2 = [3, 4, 5, 6, 7]

print(test.merge(nums1, len(nums1), nums2, len(nums2)))
