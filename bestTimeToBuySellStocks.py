"""
@Abhishek 
Day 26 
Topic : Array 

"""

"""
Problem Analysis 
given array prices, prices[i] == price of stock on ith day 
find maximum profit that we can achieve 
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)

        l, r = 0, 1
        # left ptr = buy
        # right ptr = sell
        # buy low and sell high

        while r < n:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)

            else:
                l = r

            r += 1

        return maxProfit
