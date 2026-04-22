import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # me parece ser solucao que utiliza max heap
        # heapify inicial, pop 2x e push do resultado caso diff
        aux_max_heap = [-num for num in stones] # O(n)
        heapq.heapify(aux_max_heap) # O(n)
        
        while len(aux_max_heap) >= 2:
            diff = abs(-heapq.heappop(aux_max_heap) - -heapq.heappop(aux_max_heap)) # O(logn)
            if diff: heapq.heappush(aux_max_heap, -diff) # O(logn)
            print(diff)

        return -aux_max_heap[0] if aux_max_heap else 0       
    