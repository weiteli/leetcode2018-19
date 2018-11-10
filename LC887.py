class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        """
        # dp[i][j] = best relative score of subarray piles[i]~piles[j]
        n = len(piles)
        dp = [[0] * n for i in range(n)]
        
        for i in range(n):
            dp[i][i] = piles[i]
        
        for l in range(1, n):
            for i in range(0, l):
                j = l-i
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
                
        return dp[0][-1] > 0
        """
        
        n = len(piles)
        dp = piles[:]
        # Starting from 2 pair and increase
        for l in range(1, n):
            for i in range(0,l):
              dp[i] = max(piles[i] - dp[l-i], piles[l-i] - dp[i])
        return dp[-1] > 0
        
        
        
        
