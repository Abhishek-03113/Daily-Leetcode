"""
@Abhishek 
Day 32 : Daily Challenge

"""


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"])
        vmap = collections.defaultdict(int)

        for x in s:
            if x in vowels:
                vmap[x] += 1

        if not vmap:
            return s

        sorted_vowels = sorted(vmap.keys(), key=lambda x: ord(x))

        l = 0
        t = ""

        for x in s:
            if x not in vowels:
                t += x
            else:
                vmap[sorted_vowels[l]] -= 1
                t += sorted_vowels[l]
                if vmap[sorted_vowels[l]] == 0:
                    del vmap[sorted_vowels[l]]
                    l += 1
        return t
