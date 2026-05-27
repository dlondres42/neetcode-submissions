from typing import Optional
from collections import deque

class PrefixNode:
    def __init__(self, value: Optional[int], name: Optional[str]) -> None:
        self.children = {}
        self.value = value
        self.name = name


class FileSystem:

    def __init__(self):
        self.root = PrefixNode(None,None)


    def createPath(self, path: str, value: int) -> bool:
        curr_node = self.root
        path_split = deque(path.split('/'))
        path_split.popleft()
        print(path_split)
        
        if len(path_split) == 1:
            if path_split[0] in curr_node.children:
                return False
            curr_node.children[path_split[0]] = PrefixNode(value, path_split[0])
            return True

        for i in range(0,len(path_split)):
            if i == len(path_split) - 1: break
            if path_split[i] not in curr_node.children:
                return False
            print(f"{curr_node.children} inside {curr_node.name}")
            curr_node = curr_node.children[path_split[i]]
        
        if path_split[i] in curr_node.children:
                return False

        curr_node.children[path_split[i]] = PrefixNode(value, path_split[i])
        print(curr_node.children)
        return True

    def get(self, path: str) -> int:
        curr = self.root
        path_split = deque(path.split('/'))
        path_split.popleft()
        
        for word in path_split:
            if word not in curr.children:
                return -1
            curr = curr.children[word]

        return curr.value


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
