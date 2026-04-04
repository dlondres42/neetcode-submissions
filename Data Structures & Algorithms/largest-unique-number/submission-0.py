class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        largest = -1
        nums.sort()

        for num in nums[::-1]:
            if num == largest: largest = -1
            else: largest = max(num, largest)

        return largest