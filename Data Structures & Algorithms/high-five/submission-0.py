import heapq
from sortedcontainers import SortedDict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        aux_map = SortedDict() # armazena id + top5 

        for student, grade in items:
            if student not in aux_map:
                aux_map[student] = [grade]
            else:
                if len(aux_map[student]) < 5:
                    heapq.heappush(aux_map[student], grade)
                else:
                    if grade > aux_map[student][0]:
                        heapq.heappop(aux_map[student])
                        heapq.heappush(aux_map[student], grade)

        #print(aux_map)       



        return [[key,sum(aux_map[key])//5] for key in aux_map.keys()]