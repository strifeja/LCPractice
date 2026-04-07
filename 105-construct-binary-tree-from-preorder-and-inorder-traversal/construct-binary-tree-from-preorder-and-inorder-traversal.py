# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        root_index = inorder.index(root.val)

        left_tree = inorder[0:root_index]
        right_tree = inorder[root_index+1:]

        left_size = len(left_tree)

        left_pre = preorder[1:1 + left_size]
        right_pre = preorder[1 + left_size:]

        root.left = self.buildTree(left_pre, left_tree)
        root.right = self.buildTree(right_pre, right_tree)

        return root