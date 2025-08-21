class Solution(object):
    def productExceptSelf(self, nums):
        a = [1]*len(nums)
        lp = 1
        rp = 1

        for i in range(len(nums)):
            a[i] *= lp
            lp *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            a[i] *= rp
            rp *= nums[i]
        return a

