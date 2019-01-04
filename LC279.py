class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        dp = [9999]*(n+1)
        
        idx = 1
        while idx*idx <= n:
            dp[idx*idx] = 1
            idx += 1
        
        for i in range(2, n+1):
            if dp[i] == 1:
                continue
            for j in range(1, i):
                dp[i] = min(dp[i], dp[j]+dp[i-j])
                
        return dp[n]
        '''
        
        if n == 0:
            return 0
        
        dp = [9999]*(n+1)
        dp[0] = 0
        dp[1] = 1
        
        #for all n can be written as = a*a + b*b + c*c + d*d
        for i in range(2, n+1):
            j = 1
            while (j*j <= i):
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[-1]
        
            
