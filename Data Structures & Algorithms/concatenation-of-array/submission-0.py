class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_array = [0 for _ in range(0, 2 * len(nums))]

        for i in range(0, len(nums)):
            new_array[i] = nums[i]
            new_array[i+ len(nums)] = nums[i]
    
        return new_array