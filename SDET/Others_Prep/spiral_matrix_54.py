
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        res = []

        while left <= right and top <= bottom:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top = top+1
                
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right = right-1

            if not (left <= right and top <= bottom):
                break

            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom = bottom-1

            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left = left+1
        return res