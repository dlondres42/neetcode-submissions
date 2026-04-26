class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1,n + 1)]
        result = []
        def solve(i, combination, nums):
            if i == len(nums):
                if len(combination) == k:
                    result.append(combination[:])
                return
            combination.append(nums[i])
            solve(i + 1, combination, nums)
            combination.pop()
            solve(i + 1, combination, nums)

        solve(0, [], nums)

        return result