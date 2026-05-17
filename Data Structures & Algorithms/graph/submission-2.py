class Graph:
    
    def __init__(self):
        self.aux_dict = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src in self.aux_dict:
            self.aux_dict[src].add(dst)
        else:
            self.aux_dict[src] = set([dst])

        if dst not in self.aux_dict: self.aux_dict[dst] = set()

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.aux_dict: return False
        if dst not in self.aux_dict[src]: return False

        self.aux_dict[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()

        def dfs(curr_edge):
            if curr_edge in visit: return False
            if curr_edge == dst: return True
            flag = False
            visit.add(curr_edge)
            for node in self.aux_dict[curr_edge]:
                flag = dfs(node)
                if flag: break
            
            return flag 
        
        return dfs(src)


    def __repr__(self) -> str:
        return f"{self.aux_dict}"
