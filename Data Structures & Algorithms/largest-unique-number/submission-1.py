class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        aux_map = {}
        for num in nums:
            if num not in aux_map: aux_map[num] = 1
            else: aux_map[num] += 1

        largest = -1
        for key in aux_map.keys():
            if aux_map[key] == 1: largest = max(largest, key)

        return largest