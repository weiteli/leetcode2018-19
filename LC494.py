class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        array_length = 2*total + 1
        
        if S > total:
            return 0
        
        dp =[0]* array_length
        dp[total] = 1
        
        for i in nums:
            tmp = [0]*array_length
            for j in range(array_length):
                if dp[j] != 0:
                    tmp[j+i] += dp[j]
                    tmp[j-i] += dp[j]
            dp = tmp
        
        return dp[S+total]
                
            
        
        
