import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        aux_min_heap = []
        for i, num in enumerate(nums):
            aux_min_heap.append((num, i))

        heapq.heapify(aux_min_heap)

        for _ in range(0, k): # O(k)
            value, position = heapq.heappop(aux_min_heap)
            nums[position] = value * multiplier
            heapq.heappush(aux_min_heap, (value * multiplier, position))

        return nums