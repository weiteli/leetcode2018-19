class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        """
        if len(A) == 0 or len(B) == 0:
            return 0
        
        max_length = 0
        
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    loc_a, loc_b = i, j
                    cur_length = 0
                    while(A[loc_a] == B[loc_b]):
                        loc_a += 1
                        loc_b += 1
                        cur_length += 1
                        if loc_a == len(A) or loc_b == len(B):
                            break
                    
                    if cur_length > max_length:
                        max_length = cur_length
        
        return max_length
        """
        
        m, n = len(A), len(B)
        dp = [[0] * (n+1) for i in range(m+1)]
        
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        return res
        
        
        
                
