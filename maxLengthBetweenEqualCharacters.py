class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        # ans = -1        
        # for i in range(len(s)):
        #     for j in range(i+1,len(s)):

        #         if s[i] == s[j]:
        #             ans = max(ans, j - i -1 )
        # return ans

        # ans = -1 

        # map = defaultdict(list)

        # for i in range(len(s)):

        #     map[s[i]] += [i]
        
        # for i in map:

        #     if len(map[i]) == 1:
        #         continue 
            
        #     ans = max((map[i][-1]- map[i][0]-1 ), ans)

        # return ans 

        first_index = {} 

        ans = -1 

        for i in range(len(s)):

            if s[i] not in first_index:
                first_index[s[i]] = i 
            else:

                ans = max(ans, i - first_index[s[i]] - 1)
           
        return ans
