class Solution:
    def findCircleNum2(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = [0] * len(M)
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                self.DFS_recursive(M, i, visited)
                count += 1
        return count
        
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = [0] * len(M)
        count = 0
        
        for start in range(len(M)):
            if visited[start] == 1:
                continue
            stack = [start]    
            while len(stack) != 0:
                end = stack.pop()
                if visited[end] ==0:
                    visited[end] = 1                            
                    for i in range(len(M)):
                        if M[end][i] == 1 and visited[i] == 0:
                            stack.append(i)
            count += 1
        return count
    
    def DFS_recursive(self, M, start, visited):
        for i in range(len(M)):
            if i == start:
                visited[i] == 1
                continue
                
            if visited[i]==0 and M[start][i] == 1:
                visited[i] = 1
                self.DFS_recursive(M, i, visited)
        
            
