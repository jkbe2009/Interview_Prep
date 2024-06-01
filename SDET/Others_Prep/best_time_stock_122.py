
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit, total_profit = 0, 0
        min_price = float("inf")

        for price in prices:
            min_price = min(min_price, price)
            # If selling:
            if price > min_price:
                profit = price-min_price
                total_profit += profit
                min_price = price
        
        return total_profit