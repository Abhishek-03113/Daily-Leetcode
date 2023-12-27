class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # s1 = ''.join(word1) 
        # s2 = ''.join(word2) 
        # return s1==s2

        return all(starmap(eq, zip_longest(chain.from_iterable(word1), chain.from_iterable(word2))))
