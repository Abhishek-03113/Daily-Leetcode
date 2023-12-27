from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        s = int(25*n/100)
        d = Counter(arr)
        


        for i in d:

            if d[i] > s:
                return i 
        
            
