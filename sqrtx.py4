"""
@Abhishek 

Day 6 Problem 2 
Squareroot of a number without using built in function 

"""


class Solution(object):
    def mySqrt(self, n):
        """
        :type x: int
        :rtype: int
        """
        if n < 2:
            return n
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == n:
                return mid
            elif mid * mid < n:
                low = mid + 1
            else:
                high = mid - 1
        return high
