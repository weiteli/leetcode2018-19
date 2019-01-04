class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        
        dp = [[0]*N for i in range(N)]
        dp[r][c] = 1
        
        for i in range(K):
            tmp = [[0]*N for i in range(N)]
            for a in range(N):
                for b in range(N):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        
                        if 0<= a+dr < N and 0<= b+dc < N:
                            tmp[a+dr][b+dc] += dp[a][b]/8.0
                            
            dp = tmp
            
        return sum(map(sum, dp))
        
