from _heapq import heappushpop
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # solucao com sort seria O(nlogn) onde n é o tamanho da lista
        # possivel fazer melhor com min heap onde k eh o tamanho da heap
        # ficando O(nlogk) com O(k) pra memoria; solucao com min heap performa
        # O(nlogn) com O(n) para memoria

        aux_min_heap = []

        for num in nums:
            if len(aux_min_heap) < k:
                heapq.heappush(aux_min_heap, num) # O(logn)
            else:
                if num > aux_min_heap[0]:
                    heapq.heappop(aux_min_heap) # O(1)
                    heapq.heappush(aux_min_heap, num)

            #print(aux_min_heap)

        return heapq.heappop(aux_min_heap)