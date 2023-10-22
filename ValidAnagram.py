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
