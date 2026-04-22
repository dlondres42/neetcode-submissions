import math
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # uma max heap aqui resolve, constantemente fazendo 
        # pop e pull; deve encerrar apos k ops

        aux_max_heap = [-num for num in gifts]
        heapq.heapify(aux_max_heap) # O(n)

        while k:
            temp = math.floor(sqrt(-heapq.heappop(aux_max_heap))) # O(1)
            heapq.heappush(aux_max_heap, -temp) # O(logn)
            #print(aux_max_heap)
            k -= 1

        return -sum(aux_max_heap) 