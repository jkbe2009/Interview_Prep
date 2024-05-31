
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Validate rows:

        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item == '.':
                    continue
                if item in s:
                    return False
                else:
                    s.add(item)

        # Validate cols:

        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item == '.':
                    continue
                if item in s:
                    return False
                else:
                    s.add(item)
        
        # Validate matrix:

        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                s = set()
                for i in range(3):
                    for j in range(3):
                        item = board[x+i][y+j]
                        if item == '.':
                            continue
                        if item in s:
                            return False
                        else:
                            s.add(item)

        start = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        for x, y in start:
            s = set()
            for i in range(3):
                for j in range(3):
                    item = board[x+i][y+j]
                    if item == '.':
                        continue
                    if item in s:
                        return False
                    else:
                        s.add(item)
        
        return True