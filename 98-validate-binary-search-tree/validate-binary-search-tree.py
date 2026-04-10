# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(node, left, right):
            if not node:
                return True
            if not(left < node.val < right):
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        
        return dfs(root, float('-inf'), float('inf'))


        # if not root:
        #     return True
        # elif root.left and root.right:
        #     if root.left.val >= root.val or root.right.val <= root.val:
        #         return False
        # elif root.left:
        #     if root.left.val >= root.val:
        #         return False
        # elif root.right:
        #     if root.right.val <= root.val:
        #         return False
        
        

        # return self.isValidBST(root.left) and self.isValidBST(root.right)
        