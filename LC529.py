class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        self.adjs = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,-1), (-1,1)]
        self.DFS(board, click[0], click[1])
        
        return board
    
    # M --> unrevealed boom
    # E --> unrevealed empty
    # B --> revealed empty
    def DFS(self, board, row, col):
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return
    
        if board[row][col] == 'E':
            #
            neighbor_M = 0
            e_list = []
            for r,c in self.adjs:
                if 0<= row+r < len(board) and 0<= col+c < len(board[0]):
                    if board[row+r][col+c] == 'M':
                        neighbor_M += 1
                        
                    elif board[row+r][col+c] == 'E':
                        e_list.append((row+r, col+c))
            
            if neighbor_M == 0:
                board[row][col] = 'B'
                for r, c in e_list:
                    self.DFS(board, r, c)
            else:
                board[row][col] = str(neighbor_M)
                
            
