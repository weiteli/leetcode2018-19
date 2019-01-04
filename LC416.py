class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        total = sum(nums)
        if total%2 == 1:
            return False
        
        target = total/2 + 1
        '''
        dp = [[False]*target for i in range(len(nums))]
        
        for i in range(len(nums)):
            dp[i][0] = True
        
        for i in range(1, len(nums)):
            for j in range(1, target):
                # if get true using smaller number of nums[i], still true
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]
        return dp[-1][-1]
        '''
        
        dp = [False]*target
        dp[0] = True
        for i in range(len(nums)):
            for j in range(target-1, -1, -1):
                if j >= nums[i]:
                    dp[j] = dp[j] | dp[j-nums[i]]
            
        
        return dp[-1]
        
