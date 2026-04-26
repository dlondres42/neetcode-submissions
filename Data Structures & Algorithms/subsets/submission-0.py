import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def iterate(i, nums, curr_set):
            if i == len(nums):
                return
            curr_set.append(nums[i])
            result.append(curr_set[:])
            iterate(i + 1, nums, curr_set)
            curr_set.pop()
            iterate(i + 1, nums, curr_set)

        iterate(0, nums, [])
        result.append([])
        return result