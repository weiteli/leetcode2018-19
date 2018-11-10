class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
       
        for i in range(1, n):
            for j in range(0, n):
                if j== 0:
                    A[i][j] = A[i][j] + min(A[i-1][j], A[i-1][j+1])
                elif j == n-1:
                    A[i][j] = A[i][j] + min(A[i-1][j], A[i-1][j-1])
                else:
                    A[i][j] = A[i][j] + min(A[i-1][j], A[i-1][j+1], A[i-1][j-1])
        
        return min(A[n-1])
