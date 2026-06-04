class Solution:
    def tribonacci(self, n: int) -> int:

        aux_map = {}        

        def solve(n, aux_map):
            if n <= 1: return n
            if n == 2: return 1
            if n in aux_map: return aux_map[n]

            aux_map[n] = solve(n - 1, aux_map) + solve(n - 2, aux_map) + solve(n-3, aux_map)
            print(aux_map)
            return aux_map[n]

        return solve(n, aux_map)