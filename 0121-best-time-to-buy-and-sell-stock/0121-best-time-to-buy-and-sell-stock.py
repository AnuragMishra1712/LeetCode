class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest = prices[0]
        profit = 0

        for p in prices:
            if lowest>p:
                lowest = p
            profit = max(profit,p-lowest)
        return profit        
        