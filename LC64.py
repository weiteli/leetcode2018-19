class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0]*n for i in range(m)]
        
        for row in range(m):
            for col in range(n):
                if row == 0:
                    dp[row][col] = dp[row][col-1] + grid[row][col]
                elif col == 0:
                    dp[row][col] = dp[row-1][col] + grid[row][col]
                else:
                    dp[row][col] = grid[row][col] + min(dp[row][col-1], dp[row-1][col])
        
        return dp[m-1][n-1]
                    
        
