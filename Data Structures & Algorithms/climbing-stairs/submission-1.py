class Solution: 
    def climbStairs(self, n: int) -> int: 
        total_steps = 0 
        memo = {} 
        def take_steps(n): 
            if n == 0: return 1 
            if n == 1: return 1 
            if n in memo: return memo[n] 
            total_steps = take_steps(n - 1) + take_steps(n - 2) 
            memo[n] = total_steps 
            return total_steps 
         
 
        return take_steps(n)