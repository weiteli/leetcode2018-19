class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        a = nums[0]
        b = max(nums[0], nums[1])
        
        if len(nums) == 2:
            return max(a,b)

        for i in range(2, len(nums)):
            amt = max(nums[i] + a, b)
            a = b
            b = amt
        
        return b
