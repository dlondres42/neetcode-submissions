class Solution:
    def mySqrt(self, x: int) -> int:
        # fazer busca binaria comecando de x/2 como right
        # precisa de um high para ver o ultimo numero maior que x
        # mid seria x/4
        
        left = 1
        right = x
        mid = (left + right) // 2
        while mid != right and mid != left:
            #print(f"{left}, {mid}, {right}")
            if mid ** 2 < x:
                left = mid
            elif mid ** 2 > x:
                right = mid
            else: break
            mid = (left + right) // 2

        return mid
            