
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy_p = float("inf")

        for price in prices:
            buy_p = min(buy_p, price)
            profit = price-buy_p
            max_profit = max(max_profit, profit)
        
        return max_profit