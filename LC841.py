class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        if len(rooms[0]) == 0:
            if len(rooms) == 1:
                return True
            return False
        
        stack = [rooms[0]]
        N = len(rooms)
        visited = [0]*N
        visited[0] = 1
        while len(stack) != 0:
            keys = stack.pop()
            for key in keys:
                visited[key] = 1
                if len(rooms[key]) != 0:
                    stack.append(rooms[key])
                    rooms[key] = []
        
        if sum(visited) == N:
            return True
        else:
            return False
            
            
            
        
