class Solution:
    def totalMoney(self, n: int) -> int:

        # ans = 0
        # monday = 1
        
        # while n > 0:
        #     for day in range(min(n, 7)):
        #         ans += monday + day
            
        #     n -= 7
        #     monday += 1

        # return ans


        k = n // 7
        F = 28
        L = 28 + (k - 1) * 7
        arithmetic_sum = k * (F + L) // 2
        
        monday = 1 + k
        final_week = 0
        for day in range(n % 7):
            final_week += monday + day
        
        return arithmetic_sum + final_week

             

