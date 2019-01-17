class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.num_row, self.num_col = len(image), len(image[0])
        self.newColor = newColor
        self.orgColor = image[sr][sc]
        
        if self.newColor != self.orgColor:
            self.DFS2(sr, sc, image)
        
        return image
        
    def DFS(self, row, col, image):
        if not (0 <= row < self.num_row and 0 <=col<self.num_col) or image[row][col] != self.orgColor:
            return
        
        image[row][col] = self.newColor
        [self.DFS(row+r, col+c, image) for (r,c) in [(0,1), (0,-1), (1,0), (-1,0)]]
    
                
    def DFS2(self, row, col, image):
        if row < 0 or row >= self.num_row or col < 0 or col >= self.num_col:
            return
        if image[row][col] != self.orgColor:
            return
        
        image[row][col] = self.newColor
        
        self.DFS2(row+1, col, image)
        self.DFS2(row-1, col, image)
        self.DFS2(row, col+1, image)
        self.DFS2(row, col-1, image)
        
        return
        
