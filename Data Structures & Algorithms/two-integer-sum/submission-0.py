class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        auxMap = {}
        for position, num in enumerate(nums):
            expectedValue = target - num

            if expectedValue in auxMap:
                return [auxMap[expectedValue], position]

            if num not in auxMap:
                auxMap[num] = position
        