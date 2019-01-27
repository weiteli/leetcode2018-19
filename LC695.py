class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.n = len(grid)
        self.m = len(grid[0])
        max_area = 0
        
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j]:
                    max_area = max(max_area, self.dfs(i, j))
        return max_area

    def dfs(self,i, j):
        if (0 <= i < self.n) and (0<=j<self.m):
            if self.grid[i][j]:
                self.grid[i][j]=0
                return self.dfs(i + 1, j) + self.dfs(i - 1, j) + self.dfs(i, j + 1) + self.dfs(i, j - 1) + 1
        return 0
        
