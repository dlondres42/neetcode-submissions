import heapq

class KthLargest:
    # usar min heap de alguma forma
    # seria o equivalente a usar nlargest(heap, k)
    # mas implementando na mao pra melhor performance de memoria
    def __init__(self, k: int, nums: List[int]):
        self.aux_heap = []
        self.max_size = k
        for num in nums:
            if len(self.aux_heap) < self.max_size:
                heapq.heappush(self.aux_heap, num)
            else:
                if num > self.aux_heap[0]:
                    heapq.heappushpop(self.aux_heap, num) # O(2 * logk)

    def add(self, val: int) -> int:
        if len(self.aux_heap) < self.max_size:
            heapq.heappush(self.aux_heap, val)
        else:
            if val > self.aux_heap[0]:
                heapq.heappushpop(self.aux_heap, val)

        return self.aux_heap[0]