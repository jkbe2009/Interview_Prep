"""

Search in a Binary Search Tree

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        def recursive_imp(root,val):
            if root == None:
                return None
            
            if val == root.val:
                return root
            elif val < root.val:
                return self.searchBST(root.left, val)
            else:
                return self.searchBST(root.right, val)

        def iterative_imp(root,val):
            while root:
                if val == root.val:
                    return root
                elif val < root.val:
                    root = root.left 
                else:
                    root = root.right
            return None
        
        # return recursive_imp(root,val)
        return iterative_imp(root,val)