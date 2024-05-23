
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None or (root.left == None and root.right == None):
            return root
        
        q = deque()
        curr = root
        q.append(curr)

        while q:
            node = q.popleft()
            left = node.left
            right = node.right
            node.left = right
            node.right = left
            if left: 
                q.append(left)
            if right:
                q.append(right)
            
        
        return root


        