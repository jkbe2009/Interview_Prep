
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        i , j = 0, len(matrix)-1
        while i < j:
            for ind in range(len(matrix)):
                matrix[i][ind], matrix[j][ind] = matrix[j][ind], matrix[i][ind]
            i += 1
            j -= 1 

        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                if i == j:
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]             