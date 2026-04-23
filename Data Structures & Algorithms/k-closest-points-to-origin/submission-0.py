import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap armazena a distancia e 
        # o indice do ponto na lista, faz pop 
        # k vezes para pegar o k menor
        aux_min_heap = []

        for point in points: # O(n)
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(aux_min_heap, (distance, point)) # O(logn)
            #print((distance, point))
        
        result = [heapq.heappop(aux_min_heap)[1] for _ in range(0, k)] # O(k) 

        return result
