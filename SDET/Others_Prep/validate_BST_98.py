
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """

        First Version:
        --------------

        if not root:
            return True
        
        if (root.left and root.left.val >= root.val) or (root.right and root.right.val <= root.val):
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)
        
        
        # Second Version:
        # --------------
        
        def get_min(root):
            if not root.left:
                return root.val
            return get_min(root.left)
            
        
        def get_max(root):
            if not root.right:
                return root.val
            return get_max(root.right)
            
        if not root:
            return True

        if (root.left and get_max(root.left) >= root.val) or (root.right and get_min(root.right) <= root.val):
            return False
        else:
            return self.isValidBST(root.left) and self.isValidBST(root.right)

        """
        # Third Version:
        # --------------
        def is_valid(root, left, right):
            if not root:
                return True
            
            if not (root.val > left and root.val < right):
                return False

            return is_valid(root.left, left, root.val) and is_valid(root.right, root.val, right)

        return is_valid(root, float("-inf"), float("inf"))