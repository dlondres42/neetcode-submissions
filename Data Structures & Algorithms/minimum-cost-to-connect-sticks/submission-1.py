import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        result = 0
        if len(sticks) == 1: return 0
        heapq.heapify(sticks) # O(n)
        
        while len(sticks) > 1: #O(n)
            intermediate_result = heapq.heappop(sticks) + heapq.heappop(sticks) # O(logn)
            heapq.heappush(sticks, intermediate_result) #O(logn)
            result += intermediate_result
            #print(sticks)

        #total O(nlogn)

        return result      