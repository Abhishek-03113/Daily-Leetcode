class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = defaultdict() 

        for i in range(len(s)): 

            seen[s[i]] = 1 + seen.get(s[i], 0) 
        

        for n,i in enumerate(s): 
            if seen[i] == 1: 
                return n
            
        
        return -1 

