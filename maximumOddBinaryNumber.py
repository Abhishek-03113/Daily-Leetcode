class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = sorted(s, reverse=True) 

        for i in range(len(s)-1,-1,-1):

            if s[i] == '1':
                s[i], s[-1] = s[-1], s[i] 
                break 
        return ''.join(s)
