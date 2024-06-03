
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = set()

        def helper(ind, i, j):
            # Base Case:
            if ind == len(word):
                return True
            
            if ((i, j) in visited or i < 0 or i >= len(board) or
                j < 0 or j >= len(board[i]) or word[ind] != board[i][j]):
                return False
            
            # Recursive Case:
            visited.add((i, j))
            ans = (
                helper(ind+1, i, j+1) or
                helper(ind+1, i, j-1) or
                helper(ind+1, i+1, j) or
                helper(ind+1, i-1, j)
            )
            visited.remove((i, j))
            return ans
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if helper(0, i, j):                
                    return True
        
        return False
                