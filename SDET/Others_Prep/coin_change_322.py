
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        """
        Recursive solution with memoization:
        ------------------------------------

        results = {}

        def helper(ind, count, total):
            # Base case:
            if total == amount:
                return count

            if total > amount or ind >= len(coins):
                return float("inf")
            
            # Recursive case:
            if amount-total in results and results[amount-total] <= count:
                return results[amount-total]

            ans1 = helper(ind, count+1, total+coins[ind])
            ans2 = helper(ind+1, count, total)
            ans = min(ans1, ans2)
         
            results[amount-total] = ans
            return ans

        coins.sort(reverse = True)
        ans = helper(0, 0, 0)
        return -1 if ans == float("inf") else ans
        
        """
        
        """
        Greedy approach:
        ----------------

        coins.sort()
        count = 0
        for i in range(len(coins)-1, -1, -1):
            while (coins[i] <= amount):
                amount -= coins[i]
                count += 1
                
        return count if amount == 0 else -1
        
        """

        # Dynamic programming solution:

        dp = [0] * (amount+1)

        for amt in range(1, amount+1):
            dp[amt] = float("inf")
            for coin in coins:
                if coin <= amt and dp[amt-coin] != float("inf"):
                    dp[amt] = min(1 + dp[amt-coin], dp[amt])
        
        return dp[amount] if dp[amount] != float("inf") else -1
