
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = deque()
        res = []

        q.append(root)

        while q:
            li = []
            for i in range(len(q)):
                node = q.popleft()
                li.append(node.val)
                left = node.left
                right = node.right
                if left:
                    q.append(left)
                if right:
                    q.append(right)
            res.append(li)
        return res

