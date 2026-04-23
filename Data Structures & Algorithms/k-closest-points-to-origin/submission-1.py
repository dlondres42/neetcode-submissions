import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # usando max heap para nao passar de
        # k elementos
        aux_max_heap = []
        
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            if len(aux_max_heap) < k:
                heapq.heappush(aux_max_heap, (-distance, point))
            else:
                if -distance > aux_max_heap[0][0]:
                    heapq.heappop(aux_max_heap) # O(1)
                    heapq.heappush(aux_max_heap, (-distance, point))

            #print(aux_max_heap)

        return [heapq.heappop(aux_max_heap)[1] for _ in range(0, k)]