"""
@Abhishek
Day 19 
Topic : Hashmap
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jwls = dict()
        jwls[jewels] = 0

        for i in stones:
            if i in jewels:
                jwls[jewels] += 1

        return jwls[jewels]
