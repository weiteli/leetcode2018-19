class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = [[0]*(m+1) for i in range(n+1)]
        for s in strs:
            num_z, num_o = 0, 0
            for c in s:
                if c == '0':
                    num_z += 1
                else:
                    num_o += 1
            
            for i in range(n, num_o-1, -1):
                for j in range(m, num_z-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-num_o][j-num_z]+1)
                    
        return dp[n][m]
