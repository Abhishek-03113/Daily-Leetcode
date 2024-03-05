class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)

        ans =0
        l, r = 0, n-1 
        while l < r and s[l] == s[r]:
            char = s[l]

            while l <= r and s[l] == char:
                l += 1
            while r >= l and s[r] == char:
                r -= 1
            
        ans = r - l + 1

        return ans 
            

        
