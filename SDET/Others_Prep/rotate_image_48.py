
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1 : Transpose matrix:
        for i in range(rows):
            for j in range(i+1, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2 : reverse columns of the matrix:
        for i in range(rows):
            l, r = 0, cols-1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1
        
        return