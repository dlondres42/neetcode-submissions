class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_heights = sorted(heights)
        result = 0

        for i in range(len(heights)):
            if heights[i] != new_heights[i]: result += 1

        return result
