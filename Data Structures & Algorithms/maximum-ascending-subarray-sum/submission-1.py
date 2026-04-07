class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = 0
        i = 1
        if len(nums) == 1: return curr_sum
        
        while i < len(nums):
            max_sum = max(curr_sum, max_sum)
            if nums[i-1] < nums[i] :
                curr_sum += nums[i] 
            else:
                curr_sum = nums[i]
            print(curr_sum)
            max_sum = max(curr_sum, max_sum)
            i += 1

        return max_sum