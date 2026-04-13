class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        def value_check(index, val, arrval):
            if val == arrval:
                return index
            else:
                return -1

        left, right = 0, len(nums) - 1
        result = []

        while left < right:
            mid = (right + left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        result.append(value_check(left, nums[left], target))

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        
        result.append(value_check(left, nums[left], target))

        return result


        

        