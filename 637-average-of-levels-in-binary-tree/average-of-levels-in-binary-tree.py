# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        result = []
        currSum, currElement = 0, 0

        queue = deque([root])
        queue.append(None)

        while queue:
            node = queue.popleft()
            if not node:
                result.append(float(currSum) / float(currElement))
                if queue:
                    queue.append(None)
                    currSum = 0
                    currElement = 0
                   
            else:
                currSum += node.val
                currElement += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result