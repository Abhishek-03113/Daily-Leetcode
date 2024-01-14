class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        n, m = len(word1), len(word2) 

        if m!=n:
            return False

        
        chars_w1 = [0] * 26 
        chars_w2 = [0] * 26 


        for i in range(m):
            chars_w1[ord(word1[i]) - ord('a')] += 1 

            chars_w2[ord(word2[i]) - ord('a')] += 1

        
        for i in range(26):

            if (chars_w1[i] == 0 and chars_w2[i] != 0) or (chars_w1[i] != 0 and chars_w2[i] == 0):
                return False
        
        chars_w1.sort() 
        chars_w2.sort() 


        for i in range(26):

            if chars_w1[i] != chars_w2[i]:
                return False
            
        return True 
