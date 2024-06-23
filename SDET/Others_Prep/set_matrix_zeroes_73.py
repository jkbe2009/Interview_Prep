
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        change = set()

        def add_cord(i, j):
            for k in range(rows):
                change.add((k, j))
            for k in range(cols):
                change.add((i, k))
            return

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    add_cord(i,j)
        
        for i, j in change:
            matrix[i][j] = 0
        
        return