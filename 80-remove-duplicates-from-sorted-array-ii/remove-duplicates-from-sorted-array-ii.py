class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, n = 0, len(nums)

        for j in range(n):
            if i < 2 or nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
        return i
        
        