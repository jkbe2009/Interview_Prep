
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        visited = set()

        def dfs(i, j):
            # Edge case:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0" or (i,j) in visited:
                return
            
            grid[i][j] = "0"
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
            return

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)

        return res