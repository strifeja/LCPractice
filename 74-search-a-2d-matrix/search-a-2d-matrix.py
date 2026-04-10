class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flat = [x for row in matrix for x in row]
        left = 0
        right = len(flat) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if target == flat[mid]:
                return True
            elif flat[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        