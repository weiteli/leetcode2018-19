class Solution(object):
    """
    def PredictTheWinner(self, nums):
        return self.getScore(nums, 0, len(nums)-1) >= 0
        
    def getScore(self, nums, l, r):
        if l == r: return nums[l]
        return max(nums[l] - self.getScore(nums, l+1, r), nums[r] - self.getScore(nums, l, r-1))
    """    
    
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[0]*n for i in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for j in range(1, n):
            for l in range(j, 0, -1):
                i = l-1 
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        return dp[0][-1] >= 0
