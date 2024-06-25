
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        """
        # Brute Force solution: dfs without trie

        visited = set()
        res = set()

        def helper(ind, i, j, word):
            # Base Case:
            if ind == len(word):
                return True
            
            if ((i, j) in visited or i < 0 or i >= len(board) or
                j < 0 or j >= len(board[i]) or word[ind] != board[i][j]):
                return False
            
            # Recursive Case:
            visited.add((i, j))
            ans = (
                helper(ind+1, i, j+1, word) or
                helper(ind+1, i, j-1, word) or
                helper(ind+1, i+1, j, word) or
                helper(ind+1, i-1, j, word)
            )
            visited.remove((i, j))
            return ans
        
        for word in words:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if helper(0, i, j, word):
                        res.add(word)               
                    
        return list(res)
        """

        # DFS with Trie optimization:
        
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.isword = False
        
        class Trie:
            def __init__(self):
                self.root = TrieNode()
            
            def insert(self, word):
                curr = self.root

                for ch in word:
                    if ch not in curr.children:
                        curr.children[ch] = TrieNode()
                    curr = curr.children[ch]
                curr.isword = True

            def search(self, word):
                curr = self.root

                for ch in word:
                    if ch not in curr.children:
                        curr.children[ch] = TrieNode()
                    curr = curr.children[ch]
                return curr.isword
            
            def prune(self, word):
                curr = self.root
                key_to_remove = []

                for ch in word:
                    if ch not in curr.children:
                        break
                    key_to_remove.append((curr, ch))
                    curr = curr.children[ch]
 
                while key_to_remove:
                    curr, ch = key_to_remove.pop()
                    if curr.children[ch].children == {}:
                        del curr.children[ch]
                    else:
                        break
                return

                
        res = set()
        visited = set()

        obj = Trie()
        for word in words:
            obj.insert(word)
        
        # obj.prune("oath")

        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, node, temp):
            # Base case:
            if node.isword:
                res.add(temp)
                # Prune the word from the tree
                obj.prune(temp)

            if (
                i < 0 or i >= rows or j < 0 or j >= cols or
                (i, j) in visited or
                board[i][j] not in node.children
            ):
                return
           
            # Recursive case:
            visited.add((i,j))

            node = node.children[board[i][j]]
            temp = temp + board[i][j] 
        
            dfs(i, j+1, node, temp)
            dfs(i, j-1, node, temp)
            dfs(i+1, j, node, temp)
            dfs(i-1, j, node, temp)

            visited.remove((i,j))
            return

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, obj.root, "")
        
        return list(res)
                
        