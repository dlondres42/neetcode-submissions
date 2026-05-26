class PrefixNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = PrefixNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = PrefixNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word: str) -> bool:
            
        return self._dfs(self.root, 0, word)

    def _dfs(self, node: PrefixNode, index, word) -> bool:
        if node.word and index == len(word): return True
        if not node: return False
        if index == len(word): return False
        #print(f"{node.children}, {index}, {word[index]}")

        if word[index] != '.' and word[index] not in node.children:
            return False
        elif word[index] == '.':
            for key in node.children.keys():
                result = self._dfs(node.children[key], index+1, word)
                if result: return True
            return False
        else:
            return self._dfs(node.children[word[index]], index+1, word)



        
