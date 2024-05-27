
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        res = []
        visited = [[False] * len(board[0]) for i in range(len(board))]

        def helper(curr, i , j):
            # Base case:
            if curr == word:
                res.append(curr)
                return
                
            if not (i >= 0 and i < len(board)) or not (j >= 0 and j < len(board[i])):
                return

            if visited[i][j]:
                return

            if len(curr) > len(word) or (curr != "" and curr[-1] != word[len(curr)-1]):
                return
            
            # Recursive Case:
            visited[i][j] = True
            helper(curr + board[i][j], i+1 , j)
            helper(curr + board[i][j], i-1 , j)
            helper(curr + board[i][j], i , j+1)
            helper(curr + board[i][j], i , j-1)
            visited[i][j] = False

            return
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                helper("", i , j)
    
        return len(res) > 0

