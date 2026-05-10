class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        seen = set()
        ROW, COLUMN = len(grid), len(grid[0])

        def dfs(r, c, seen):
            # fazer base case
            if r < 0 or c < 0 or r >= ROW or c >= COLUMN or (r, c) in seen:
                return 0
            if grid[r][c] == 1:
                return 0
            if r == ROW - 1 and c == COLUMN - 1 and grid[r][c] == 0:
                return 1
            #passo recursivo
            seen.add((r, c))
            paths = 0
            paths += dfs(r, c + 1, seen)
            paths += dfs(r + 1, c, seen)
            paths += dfs(r - 1, c, seen)
            paths += dfs(r, c - 1, seen)
            #backtrack
            seen.remove((r,c))

            return paths

        return dfs(0, 0, seen)