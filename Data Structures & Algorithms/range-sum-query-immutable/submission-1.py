# utilizando prefix sum em vez de so somar
class NumArray:

    def __init__(self, nums: List[int]):
        curr_sum = 0
        self.sum_array = []
        for num in nums:
            curr_sum += num
            self.sum_array.append(curr_sum)
        print(self.sum_array)
    def sumRange(self, left: int, right: int) -> int:
        left_pos = self.sum_array[left - 1] if left > 0 else 0
        right_pos = self.sum_array[right]
        return right_pos - left_pos


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)