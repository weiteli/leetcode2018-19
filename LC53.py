class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
    
        if len(nums) == 1:
            return nums[0]
        
        a = nums[0]
        maximum = nums[0]
        
        for i in range(1,len(nums)):
            a = max(nums[i], nums[i]+a)
            if a> maximum:
                maximum = a
           
        return maximum
