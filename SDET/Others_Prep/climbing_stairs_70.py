
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def interative_sol(n):
            if n == 0 or n == 1:
                return 1

            a, b = 1, 1
            
            for i in range(2, n+1):
                c = a + b
                a = b
                b = c
            
            return c

        dp = [-1] * (n+1)

        def recursive_memoization(n):
            if n == 0 or n == 1:
                return 1
            
            if dp[n] != -1:
                return dp[n]

            dp[n] = recursive_memoization(n-1) + recursive_memoization(n-2)
            return dp[n]
         
        # return interative_sol(n)
        return recursive_memoization(n)