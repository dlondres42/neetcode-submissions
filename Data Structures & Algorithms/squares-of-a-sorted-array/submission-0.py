class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r = 0
        k = l = len(nums) - 1
        result = [0 for i in range(len(nums))]
        print(result)
        while r <= l:
            if nums[l] ** 2 > nums[r] ** 2:
                result[k] = nums[l] ** 2
                l -= 1
            else:
                result[k] = nums[r] ** 2
                r += 1  
            k -= 1
            #print(result)

        return result   