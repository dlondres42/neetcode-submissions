class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = {n: set() for n in range(1, n+1)} # O(n)

        for connection in trust: # O(n)
            graph[connection[0]].add(connection[1]) # O(1)

        count_dict = {}

        for key in graph.keys():
            for element in graph[key]:
                if element not in count_dict:
                    count_dict[element] = 1
                else:
                    count_dict[element] += 1

        print(count_dict)

        for key, value in count_dict.items():
            if value == n - 1 and len(graph[key]) == 0:
                return key

        return -1
