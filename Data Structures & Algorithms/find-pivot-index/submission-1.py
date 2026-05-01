class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # tentei fazer com 2 ponteiros mas muito mais
        # facil pegando a soma total e depois apenas comparar
        # com a soma prefix
        total_sum = sum(nums)
        prefix_sum = 0
        if total_sum == prefix_sum: return 0
        
        i = 0
        while i < len(nums):

            if prefix_sum == total_sum - prefix_sum - nums[i]: return i
            prefix_sum += nums[i]
            i += 1

        return -1
