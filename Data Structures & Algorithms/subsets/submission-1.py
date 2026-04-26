import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def iterate(i, nums, curr_set):
            if i == len(nums):
                result.append(curr_set[:])
                return
            
            curr_set.append(nums[i])

            iterate(i + 1, nums, curr_set)
            curr_set.pop()
            iterate(i + 1, nums, curr_set)

        iterate(0, nums, [])
        return result