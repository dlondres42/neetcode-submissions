class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1
        
        def recsolve(left, right):
            if left > right:
                return -1

            mid = (left + right) // 2
            print(f"l :{left}, r: {right}, m: {mid}")

            if nums[mid] < target:
                return recsolve(mid + 1, right)
            elif nums[mid] > target:
                return recsolve(left, mid -1)
            else:
                return mid

        return recsolve(left, right)