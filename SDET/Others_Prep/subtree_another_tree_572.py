
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def is_same_tree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        # Base case:
        if not subRoot:
            return True
        if not root:
            return False

        # Recursive case:
        return  self.is_same_tree(root, subRoot) or\
                self.isSubtree(root.left, subRoot) or\
                self.isSubtree(root.right, subRoot)