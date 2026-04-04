class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0: return False
        l = 0
        r = 1
        aux_set = set([nums[l]])
        while r < len(nums):
            if nums[r] in aux_set:
                return True
            
            aux_set.add(nums[r])
            if len(aux_set) > k:
                aux_set.remove(nums[l])
                l += 1
            r += 1
            
        return False