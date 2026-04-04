# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        mid = (1 + n) // 2
        count = 0
        print(f"l {l}, r {r}, mid {mid}")
        while guess(mid) != 0 and l < r:
            if guess(mid) > 0:
                l = mid + 1
            elif guess(mid) < 0:
                r = mid - 1
            
            mid = (l + r) // 2
            count += 1
            
        return mid