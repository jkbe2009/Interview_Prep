
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        res = []

        def dfs(i, j):
            # Base case:
            if i == m-1 and j == n-1:
                res.append(True)
                return

            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            # Recursive case:
            dfs(i, j+1)
            dfs(i+1, j)

            return
        
        def iterative():
            dp = [[1] * n for _ in range(m)]

            for i in range(1, m):
                for j in range(1, n):
                    op1 = dp[i-1][j] if i-1 >= 0 else 0
                    op2 = dp[i][j-1] if j-1 >= 0 else 0
                    dp[i][j] = op1 + op2
            return dp[m-1][n-1]


        # dfs(0, 0)
        # return len(res)

        return iterative()