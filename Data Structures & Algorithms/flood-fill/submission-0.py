class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLUMNS = len(image), len(image[0])
        old_color = image[sr][sc]
        seen = set()


        def fill(r, c, seen):
            if r < 0 or c < 0 or (r, c) in seen or r == ROWS or c == COLUMNS: return

            image[r][c] = color    
            seen.add((r,c))
            #print(np.array(image))
            #print((r,c))
            if r < ROWS - 1 and image[r + 1][c] == old_color: fill(r+1,c,seen)
            if c < COLUMNS - 1 and image[r][c + 1] == old_color: fill(r,c + 1,seen)
            if image[r - 1][c] == old_color: fill(r-1,c,seen)
            if image[r][c - 1] == old_color: fill(r,c-1,seen)
            
            seen.remove((r,c))

        fill(sr, sc, seen)
        return image