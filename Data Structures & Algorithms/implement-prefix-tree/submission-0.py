class PrefixNode:
    def __init__(self, char: str, word: bool = False):
        self.char = char
        self.word = word
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode("")
        
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            #print(curr.char)
            if char not in curr.children:
                curr.children[char] = PrefixNode(char)
            curr = curr.children[char]
        
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True
        