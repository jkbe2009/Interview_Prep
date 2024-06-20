
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        res = []

        def dfs_basic(i, j):
            # Base case:
            if (i == m-1 and j == n-1):
                res.append(True)
                return

            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            # Recursive case:
            dfs_basic(i, j+1)
            dfs_basic(i+1, j)

            return

        
        solution = [[-1] * n for _ in range(m)]

        def dfs_opt(i, j):
            # Base case:
            if (i == m-1 and j == n-1):
                return 1

            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            
            if solution[i][j] != -1:
                return solution[i][j]
            
            # Recursive case:
            ans = dfs_opt(i, j+1) + dfs_opt(i+1, j)
            solution[i][j] = ans
            return ans


        def iterative():
            dp = [[1] * n for _ in range(m)]

            for i in range(m-1, -1, -1):
                for j in range(n-1, -1, -1):
                    if i == m-1 and j == n-1:
                        continue
                    op1 = dp[i+1][j] if i+1 < m else 0
                    op2 = dp[i][j+1] if j+1 < n else 0
                    dp[i][j] = op1 + op2
            return dp[0][0]


        # dfs_basic(0, 0)
        # return len(res)

        # return dfs_opt(0 ,0)

        return iterative()