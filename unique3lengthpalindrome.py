"""
@Abhishek 
Day 33 
Topic : Hashmap, string 
"""


class Solution:
    # def countPalindromicSubsequence(self, s: str) -> int:
    #     return sum([len(set(s[s.index(letter)+1:s.rindex(letter)])) for letter in set(s)])

    # def countPalindromicSubsequence(self, s: str) -> int:
    #     letters = set(s)
    #     ans = 0

    #     for letter in letters:
    #         i, j = s.index(letter), s.rindex(letter)
    #         between = set()

    #         for k in range(i + 1, j):
    #             between.add(s[k])

    #         ans += len(between)

    #     return ans

    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        for i in range(len(s)):
            curr = ord(s[i]) - ord("a")
            if first[curr] == -1:
                first[curr] = i

            last[curr] = i

        ans = 0
        for i in range(26):
            if first[i] == -1:
                continue

            between = set()
            for j in range(first[i] + 1, last[i]):
                between.add(s[j])

            ans += len(between)

        return ans
