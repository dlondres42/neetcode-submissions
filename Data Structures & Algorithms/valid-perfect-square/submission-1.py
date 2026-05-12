class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        mid = (low + high) // 2

        while low**2 < num:
            if mid ** 2 > num:
                high = mid
            elif mid ** 2 < num:
                low = mid
            print(f"{high}, {mid}, {low}")
            mid = (low + high) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 != num and mid == low:
                return False

        return True