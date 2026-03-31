# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.min_val = float('inf')
        self.prev = None
        self.inorder(root)
        return self.min_val
       

    def inorder(self, node):
        if not node:
            return

        self.inorder(node.left)

        if self.prev is not None:
            self.min_val = min(self.min_val, node.val - self.prev)
        
        self.prev = node.val

        self.inorder(node.right)

        