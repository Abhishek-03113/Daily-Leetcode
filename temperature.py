"""
@Abhishek 
Day 9 
"""

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = [0]*2 

        ans[0] = celsius + 273.15 
        ans[1] = celsius*1.80 + 32 
        


        return ans



