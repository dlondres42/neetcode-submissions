class Solution:
    def countElements(self, arr: List[int]) -> int:
        num_sets = set(arr)
        result = 0
        for num in arr:
            if num + 1 in num_sets:
                result += 1

        return result