class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        v = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        n = len(s)
        h = n//2
        h1 = s[:h]
        h2 = s[h:]
    
        h1_v = 0 
        h2_v = 0 
        for i in range(h):
            if h1[i] in v: 
                h1_v += 1 

            if h2[i] in v: 
                h2_v += 1
        
        return h1_v == h2_v
        
        
