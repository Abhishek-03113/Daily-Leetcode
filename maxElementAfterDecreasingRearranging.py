"""
@Abhishek 
Day 33 : 
Topic : Array 
"""

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr = sorted(arr)

        # 2 operations : 
        # Decrease the value 
        # Rearrage the numbers 

        if arr[0] != 1:
                arr[0] = 1 
                
        for i in range(1,len(arr)):

            if abs(arr[i] - arr[i-1]) > 1:

                arr[i] = arr[i-1] + 1
                print(i,arr[i],arr[i-1])

                #  1 , 100 - 1 > 1 --> arr[i] = 1+1 = 2 
                #  2 , 1000 -2 > 1 --> arr[i] = 2+1 == 3 
        

        return max(arr)