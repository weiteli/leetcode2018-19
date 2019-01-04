class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        maximum = max(nums)
        dp = [0] * (maximum + 1)
        
        for n in nums:
            dp[n] += n
        
        ## Same as House Robber
        prev,maxi = 0,0
        for i in range(len(dp)):
            tmp = max(prev + dp[i], maxi)
            prev = maxi
            maxi = tmp
        
        return maxi
                       
            
            
        
        
