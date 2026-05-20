from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
       
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        queue = deque()
        seen = set()
        result = 0

        # talvez 0,0 nao seja valido, nesse caso precisa percorrer
        # ate achar celula valida
        seen.add((0,0))
        queue.append((0,0))

        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                if r == ROWS-1 and c == COLUMNS-1: return result

                directions = [(0,1), (1,0), (0,-1), (-1,0)]
                for direction in directions:
                    if min(r + direction[0], c + direction[1]) < 0 or r + direction[0] == ROWS or \
                    c + direction[1] == COLUMNS or (r + direction[0], c + direction[1]) in seen or \
                    grid[r+direction[0]][c+direction[1]] == 1:
                        continue
                    queue.append((r+direction[0], c+direction[1]))
                    seen.add((r+direction[0], c+direction[1]))
            
            result += 1

        return -1