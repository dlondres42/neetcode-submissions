class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        is_asc = True
        is_desc = True

        for i in range(1, len(nums)):
            if is_asc and nums[i] < nums[i - 1]:
                is_asc = False
                break

        for i in range(1, len(nums)):
            print(f"{is_desc}, {nums[i]}")
            if is_desc and nums[i] > nums[i - 1]:
                is_desc = False
                break

        return is_asc or is_desc