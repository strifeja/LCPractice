# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root.right and not root.left:
            return root.val
        num = str(root.val)

        def helper(s, node):
            if not node:
                return 0
            
            s += str(node.val)

            if not node.right and not node.left:
                return int(s)

            return helper(s, node.left) + helper(s, node.right)
        
        return helper(num,root.left) + helper(num,root.right)
