# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.result = 0
        self.target = k
        self.num = 0
        self.inorder(root)
        return self.result

        
    def inorder(self, node):
        if self.num >= self.target:
            return 
        if not node:
            return

        self.inorder(node.left)

        self.num = self.num + 1
        if self.num == self.target:
            self.result = node.val
        

        self.inorder(node.right)

        
