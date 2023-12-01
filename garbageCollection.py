"""
@Abhishek 
Day 39 
Topic : array 
"""

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        # array garage[i] : garbage of ith house 
        # array travel[i] : time to travel from house i to i+1 
        ans = sum(len(g) for g in garbage)
        G, P, M = False, False, False
        for i in range(len(travel), 0, -1):
            G |= 'G' in garbage[i]
            P |= 'P' in garbage[i]
            M |= 'M' in garbage[i]
            ans += travel[i-1] * (G + P + M)
        
        return ans

