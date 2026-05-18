class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # resolver com BFS
        # percorre cada posicao, se achar 1, calcula e atualiza o maximo
        max_area = 0
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        seen = set()

        def calculate_area(r,c):
            if min(r,c) < 0 or r >= ROWS or c >= COLUMNS or (r,c) in seen \
            or grid[r][c] == 0: return 0
            
            seen.add((r,c))

            return 1 + calculate_area(r + 1, c) + calculate_area(r, c + 1) + \
            calculate_area(r - 1, c) + calculate_area(r, c - 1)
            

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == '0': seen.add((r,c))
                else:
                    print(f"{(r,c)}")
                    area = calculate_area(r, c)
                    max_area = max(max_area, area)

        return max_area