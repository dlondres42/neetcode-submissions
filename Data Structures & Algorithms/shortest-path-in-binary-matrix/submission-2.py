from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # bfs comum em matriz de adjacencia, a diferencia eh ser
        # 8 direcional em vez de 4 direcional, acredito

        ROWS = len(grid)
        COLUMNS = len(grid[0])
        seen = set()
        queue = deque()
        result = 0

        if grid[0][0] == 1 or grid[ROWS-1][COLUMNS-1] == 1: return -1

        # inicializando estruturas de dados auxiliares
        queue.append((0,0))
        seen.add((0,0))

        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                
                directions = [[0,1], [1,0], [0,-1], [-1,0], [1,1], [-1,1],[-1,-1], [1,-1]]
                for direction in directions:
                    dr, dc = direction[0], direction[1]

                    if min(r + dr, c + dc) < 0 or r + dr >= ROWS or c + dc >= COLUMNS or (r + dr, c + dc) in seen or \
                    grid[r + dr][c + dc] == 1: continue
            
                    queue.append((r+dr, c+dc))
                    seen.add((r+dr, c+dc))

            result += 1
            if (ROWS-1, COLUMNS-1) in seen:
                return result + 1

        return -1
