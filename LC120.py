class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        n = len(triangle)
        '''
        # USING 2D ARRAY
        minpath = [[0]*n for i in range(n)]
        minpath[n-1] = triangle[n-1]
        
        for i in range(n-2, -1, -1):
            print(i, len(triangle[i]))
            for j in range(len(triangle[i])):
                minpath[i][j] = min(minpath[i+1][j], minpath[i+1][j+1]) + triangle[i][j]
        
        return minpath[0][0]
        '''
        # Improve space complexity using 1D array
        minpath = triangle[n-1]
        
        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                minpath[j] = min(minpath[j], minpath[j+1]) + triangle[i][j]
        
        return minpath[0]
        
