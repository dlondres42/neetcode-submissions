

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        def check_recursive(n):
            if n == 1: return True
            if round(n) != n: return False

            return check_recursive(n / 2)
            
        return check_recursive(n)