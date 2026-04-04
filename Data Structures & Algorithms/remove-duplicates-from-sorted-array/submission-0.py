class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        auxSet = set()
        k = 0
        for num in nums:
            print(auxSet)
            if num not in auxSet:
                nums[k] = num
                auxSet.add(num)
                k += 1

                

        return k