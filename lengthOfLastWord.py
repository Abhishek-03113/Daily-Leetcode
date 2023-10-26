"""
@Abhishek 
Day 16 
Topic : String, Array 
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = s.split()

        return len(arr[-1])
