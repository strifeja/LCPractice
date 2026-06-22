class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i, result, n = 0, 0, len(prices)

        for j in range(n):
            current_selling_price = prices[j] - prices[i]
            if prices[j] < prices[i]:
                i = j
            elif current_selling_price > result:
                result = current_selling_price
        return result
            