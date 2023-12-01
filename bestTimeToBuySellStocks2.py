"""
@Abhishek Pawar 
Day 27 
Topic : Array 

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # profit = 0

        # for i in range(1,n):

        #     if prices[i] > prices[i-1]:

        #         profit += prices[i]-prices[i-1]


        # return profit 
        cur_hold, cur_not_hold = -float('inf'), 0
        
        for stock_price in prices:
            
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            
			# either keep hold, or buy in stock today at stock price
            cur_hold = max( prev_hold, prev_not_hold - stock_price )
			
			# either keep not-hold, or sell out stock today at stock price
            cur_not_hold = max( prev_not_hold, prev_hold + stock_price )
            
        # maximum profit must be in not-hold state
        return cur_not_hold
