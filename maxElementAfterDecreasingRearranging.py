"""
@Abhishek 
Day 33 : 
Topic : Array 
"""

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        # arr = sorted(arr)
        # if arr[0] != 1:
        #         arr[0] = 1 
                
        # for i in range(1,len(arr)):

        #     if abs(arr[i] - arr[i-1]) > 1:

        #         arr[i] = arr[i-1] + 1        

        # return max(arr)


        # Editorial Sorting Approach : Very Optimal O(n)
        # arr.sort()
        # ans = 1
        # for i in range(1, len(arr)):
        #     if arr[i] >= ans + 1:
        #         ans += 1

        # return ans

        # Editorial Approach with no sorting 

        n = len(arr)
        counts = [0] * (n + 1)
        
        for num in arr:
            counts[min(num, n)] += 1
        
        ans = 1
        for num in range(2, n + 1):
            ans = min(ans + counts[num], num)
    
        return ans
    
        
        