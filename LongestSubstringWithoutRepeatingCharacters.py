"""
@Abhishek
Day 7 : Problem 2 

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        chars = set()
        left = 0
        length =0 

        for right in range(n):
            if s[right] not in chars:
                chars.add(s[right])
                length = max(length,right-left+1)
            else:
                while s[right] in chars:
                    chars.remove(s[left])
                    left +=1 
                chars.add(s[right])
        
        return length
        




