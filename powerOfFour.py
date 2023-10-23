"""
@Abhishek 

Day 13 
Topic : Recursion/Bit Manipulation 

"""


# how to check if a number is power of four
import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(16):
            power = 4**i

            if power == n:
                return True

            if power > n:
                return False

        return False

    def isPowerOfFour_log(self, n: int) -> bool:
        sqrt = math.sqrt(n)

        log = math.log2(sqrt)

        return log == int(log)
