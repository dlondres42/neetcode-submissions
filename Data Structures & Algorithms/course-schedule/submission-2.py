class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # problema de deteccao de ciclo
        # como detectar ciclo entre 2 nos de um grafo? 
        # representar grafo com hashmap e fazer DFS talvez

        # primeiro construir grafo
        graph = {key:set() for key in range(0, numCourses)}
        for course, prerequisite in prerequisites:
            graph[course].add(prerequisite)
        #print(graph)

        def detect_cycle(seen: set, node: int) -> bool:
            if node in seen:
                #print("achei ciclo")
                return True
            seen.add(node)
            #print(f"node {node}, seen {seen}")
            for neighbor in graph[node]:
                if detect_cycle(seen, neighbor): return True  

            seen.remove(node)

            return False

        for course in graph.keys():
            seen = set()
            has_cycle = detect_cycle(seen, course)
            if has_cycle: return False

        return True