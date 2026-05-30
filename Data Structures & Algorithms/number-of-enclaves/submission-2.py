from copy import deepcopy

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # fun auxiliar precisa calcular a area de 1s conectados e 
        # retorna caso ele encontra com a borda 
        # para nao se encontrar com a borda as celulas precisam estar entre
        # r >= 1 % r < ROWS && c >= 1 && c < COLUMNS
        # testar antes para ver

        ROWS = len(grid)
        COLUMNS = len(grid[0])
        final_result = 0
        seen = set()
        
        def dfs(r, c):
            if min(r,c) < 0 or r >= ROWS or c >= ROWS or grid[r][c] != 1 or (r,c) in seen:
                return 0

            seen.add((r,c))
            int_result = 0 

            int_result += dfs(r + 1, c)
            int_result += dfs(r, c + 1)
            int_result += dfs(r - 1, c)
            int_result += dfs(r, c - 1)

            return 1 + int_result


        # top and bottom rows (full width)
        for c in range(COLUMNS):
            if grid[0][c] == 1 and (0, c) not in seen: dfs(0, c)
            if grid[ROWS - 1][c] == 1 and (ROWS-1, c) not in seen: dfs(ROWS-1, c)

        # left and right columns (excluding corners already done)
        for r in range(1, ROWS - 1):
            if grid[r][0] == 1 and (r, 0) not in seen: dfs(r, 0)      
            if grid[r][COLUMNS -1] == 1 and (r, COLUMNS - 1) not in seen: dfs(r, COLUMNS - 1)    

        for r in range(1, ROWS - 1):
            for c in range(1, COLUMNS - 1):
                if grid[r][c] == 1 and (r, c) not in seen:
                    result = dfs(r,c)
                    print(result)
                    final_result += result


        return final_result
