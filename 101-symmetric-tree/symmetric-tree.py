# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        return self.compare(root.left, root.right)
    
    def compare(self, left, right):
            if not left and not right:
                return True
            elif not left or not right or left.val != right.val:
                return False
            return self.compare(left.left, right.right) and self.compare(left.right, right.left)

    
        