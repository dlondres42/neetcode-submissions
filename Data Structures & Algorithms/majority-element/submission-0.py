class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        aux_map = {}
        
        for num in nums:
            if num not in aux_map:
                aux_map[num] = 1
            else:
                aux_map[num] += 1

        max_frequency = 0
        for key in aux_map.keys():
            if aux_map[key] > len(nums)//2: return key

