class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Jason Strife
        min_price = prices[0]
        total_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > 0:
                total_profit += price - min_price
                min_price = price
        
        return total_profit