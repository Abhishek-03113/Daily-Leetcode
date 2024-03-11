from collections imort defaultdict 

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # ord == unique, sorted in custom order 

        # s : i/p str  

        h = defaultdict(int) 

        for i in s: 
            h[i] = 1 + h.get(i,0) 
        
        ans = '' 

        for i in order: 
            ans += i * h[i] 

        for i in s: 

            if i not in order: 
                ans += i  
        
        return ans 
        