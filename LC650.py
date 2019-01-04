class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        if n == 0:
            return 0
        
        res = n
        for i in range(n-1, 1, -1):
            if (n % i == 0):
                res = min(res, self.minSteps(n/i)+i)
        return res
        """
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans
    
        '''
        if n == 1:
            return 0
        
        dp = [0] * (n+1)
        
        for i in range(1, n+1):
            dp[i] = i
            for j in range(n-1, 1, -1):
                if (i%j == 0):
                    dp[i] = min(dp[i], dp[j] + i/j)
                    
        return dp[-1]
        '''
