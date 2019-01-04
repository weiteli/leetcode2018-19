class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            total = 0
            for j in range(i):
                # if i == 3
                # j will iterate 0, 1, 2
                # (0, 2), (1, 1), (2,0)            
                total += dp[j]*dp[i-j-1]
            dp[i] = total
        return dp[n]
    
    
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
        """
        
        
