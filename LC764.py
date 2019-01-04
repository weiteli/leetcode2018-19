class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        banned = {tuple(mine) for mine in mines}
        
        dp = [[0]*N for i in range(N)]
        ans = 0
        
        for r in range(N):
            count = 0
            for c in range(N):
                if (r, c) in banned:
                    count = 0
                else:
                    count += 1
                dp[r][c] = count
        
            count = 0
            for c in range(N-1, -1, -1):
                if (r, c) in banned:
                    count = 0
                else:
                    count += 1
                    
                if count < dp[r][c]:
                    dp[r][c]= count
        
        for c in range(N):
            count = 0
            for r in range(N):
                if (r, c) in banned:
                    count = 0
                else:
                    count += 1
                if count < dp[r][c]:
                    dp[r][c]= count
        
            count = 0
            for r in range(N-1, -1, -1):
                if (r, c) in banned:
                    count = 0
                else:
                    count += 1
                    
                if count < dp[r][c]:
                    dp[r][c]= count
                    
                if dp[r][c] > ans:
                    ans = dp[r][c]
        
        return ans
