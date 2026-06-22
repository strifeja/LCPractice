class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, n = 0, len(nums)
        candidate = nums[0]

        for i in range(n):
            if count == 0:
                candidate = nums[i]

            if candidate == nums[i]:
                count += 1
            elif candidate != nums[i]:
                count -= 1
            
        
        return candidate


        