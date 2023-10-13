"""
@Abhishek Pawar 
Day 3: Problem 2 cuz why not 

seems complicated
"""



class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        ans = "" 
        
        strs = sorted(strs)

        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first),len(last))):

            if first[i] != last[i]:
                return ans
                
            ans += first[i]
        return ans
                
            


test = Solution()
testArr = ["flower","flow","flight"]
print(test.longestCommonPrefix(testArr))
                  
