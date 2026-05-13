class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])
        low = 0
        high = (ROWS * COLUMNS) - 1
        mid = (low + high) // 2

        print(f"{low}, {mid}, {high}")
        
        if matrix[mid//COLUMNS][mid%COLUMNS] == target or \
           matrix[high//COLUMNS][high%COLUMNS] == target or \
           matrix[low//COLUMNS][low%COLUMNS] == target:
            return True
        # como definir (r, c)?
        # dando um index entre low e high como definir (r,c) tal qual (r,c) = index
        # nao consegui pegar, mas da pra resolver (idx // COLUMNS, idx % COLUMNS)
        while low < mid < high:
            print((mid//COLUMNS, mid%COLUMNS))
            if matrix[mid//COLUMNS][mid%COLUMNS] > target:
                high = mid
            elif matrix[mid//COLUMNS][mid%COLUMNS] < target:
                low = mid
            else:
                return True
            
            mid = (low + high) // 2
            print(matrix[mid//COLUMNS][mid%COLUMNS])
            print(f"{low}, {mid}, {high}")

        return False

