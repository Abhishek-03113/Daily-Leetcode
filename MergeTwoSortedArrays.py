#!/usr/bin/python3

"""
@Abhishek 
Day 19 
Topic : Two Pointers, Array, Sorting 

"""

"""
@Abhishek 
Day 20 
Topic : Two Pointers , arrays , Sorting 

"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Built in functions

        # for j in range(n):
        #     nums1[m+j] = nums2[j]
        # nums1.sort()

        # Two pointers 
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


        
        
