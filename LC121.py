class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        
        lowest = 99999
        max_profit = 0
        
        for i in prices:
            if i < lowest:
                lowest = i
            elif (i - lowest) >  max_profit:
                max_profit = i - lowest
        
        return max_profit
