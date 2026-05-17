class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # vai percorrer por cada par (r, c) e caso encontrar 1
        # vai fazer DFS para definir a ilha, colocar as posicoes em 
        # seen e parar, depois volta ao primeiro passo
        
        seen_positions = set()
        ROWS = len(grid)
        COLUMNS  = len(grid[0])

        result = 0

        def check_island(r, c, seen_positions): # DFS
            # colocar todos 1 adjacentes em seen para nao
            # contar repetidamente no loop principal

            if r < 0 or c < 0 or c >= COLUMNS or r >= ROWS or (r, c) in seen_positions \
            or grid[r][c] == "0":
                return
            
            seen_positions.add((r,c))
            check_island(r + 1, c, seen_positions)
            check_island(r, c + 1, seen_positions)
            check_island(r - 1, c, seen_positions)
            check_island(r, c - 1, seen_positions)



        # r e c nesse loop nunca ficarao out of bounds
        for r in range(ROWS):
            for c in range(COLUMNS):
                print(f"r {r}, c {c}, grid[r][c] {grid[r][c]}")
                if (r, c) not in seen_positions and grid[r][c] == "1":
                    # quantas vezes isso disparar eh o resultado
                    print("ilha")
                    check_island(r, c, seen_positions) # adiciona todos 1 adjacentes em seen
                    result += 1
                else:
                    seen_positions.add((r,c))

        
        return result
