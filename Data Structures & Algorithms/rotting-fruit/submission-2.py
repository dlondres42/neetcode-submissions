from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # primeiro precisa achar a fruta podre
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        rotten_position = None
        seen = set()
        queue = deque()
        fruits = 0
        for row in range(ROWS): # O(n*m)
            for column in range(COLUMNS):
                if grid[row][column] == 2: 
                    rotten_position = (row,column)
                    queue.append(rotten_position)
                    seen.add(rotten_position)

                if grid[row][column] == 1:
                    fruits += 1 
        
        if len(queue) == 0 and fruits: return -1
        
        result = 0
        # com a fruta podre encontrada
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
     
                directions = [[0,1], [1,0], [0,-1], [-1,0]]
                for dr, dc in directions:
                    
                    if min(r + dr, c + dc) < 0 or r + dr >= ROWS or c + dc >= COLUMNS or \
                    grid[r+dr][c+dc] != 1 or (r+dr,c+dc) in seen: continue

                    infestation = 1
                    queue.append((r+dr, c+dc))
                    seen.add((r+dr, c+dc))
                    grid[r+dr][c+dc] = 2
                    fruits -= 1

            if len(queue) > 0:
                result += 1

        if fruits: return -1

        return result 