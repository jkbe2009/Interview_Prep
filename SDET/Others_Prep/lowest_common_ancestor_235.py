
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recursive_solution():
            if not root:
                return None
        
            if (root.val <= p.val and root.val >= q.val) or\
                (root.val <= q.val and root.val >= p.val):
                return root

            if p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return self.lowestCommonAncestor(root.left, p, q)

        def iterative_solution():
            if not root:
                return None
            
            curr = root

            while curr:
                if p.val > curr.val and q.val > curr.val:
                    curr = curr.right
                elif p.val < curr.val and q.val < curr.val:
                    curr = curr.left
                else:
                    return curr
            return None

        # return recursive_solution()
        return iterative_solution()