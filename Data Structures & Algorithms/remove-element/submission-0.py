class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        aux_list = []
        k = len(nums)

        for i, num in enumerate(nums):
            if num != val: aux_list.append(i)
            else: k -= 1
        
        nums[:k] = [nums[i] for i in aux_list]        

        return k