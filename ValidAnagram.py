"""
@Abhishek  
Day 12 : Easy 
Problem Valid Anagram 

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if set(s) != set(t):
            return False

        # Hashmap/ Dictionory Solution :

        countS, countT = {}, {}
        n = len(s)

        for i in range(n):
            countS[s[i]] = 1 + countS.get(s[i], 0)

            countT[t[i]] = 1 + countT.get(t[i], 0)

        for j in countS:
            if countS[j] != countT.get(j, 0):
                return False

        return True
        # Sorting Solution

    # return sorted(s) == sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m != n:
            return False
        
        m_len = defaultdict(int)
        n_len = defaultdict(int)


        for i in range(m):

            m_len[s[i]] = 1+ m_len.get(s[i],0)
            
            n_len[t[i]] = 1+ n_len.get(t[i],0)
        
        
        for i in m_len:

            if m_len[i] != n_len[i]:
                return False

        return True 
