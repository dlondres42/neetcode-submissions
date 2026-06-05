class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = {}
        print(cost[1])
        def solve(i):
            print(f"{i}")
            if i <= 1:
                return 0
            
            if i in cache:
                return cache[i]

            cache[i] = min(solve(i-1) + cost[i-1], solve(i-2) + cost[i-2])

            return cache[i]
                


        return solve(len(cost)) 