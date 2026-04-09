class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        aux_map = {}
        for i, num in enumerate(nums2):
            if num not in aux_map:
                aux_map[num] = i

        result = []
        for num in nums1:
            result.append(aux_map[num])
        
        return result