class Node:
    def __init__(self, key: int, value: int, left = None, right = None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Class node(key {self.key}, value {self.value})"

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root: self.root = Node(key, val)
        else:
            def insert_inner(root, key, val):
                if not root: return Node(key, val)
                else:
                    if key < root.key: root.left = insert_inner(root.left, key, val)
                    elif key > root.key: root.right = insert_inner(root.right, key, val)
                    else: root.value = val
                    return root
            root = self.root
            insert_inner(root, key, val)

    def get(self, key: int) -> int:
        root = self.root
        def get_inner(root, key) -> int:
            if not root: return -1
            if key > root.key: return get_inner(root.right, key)
            elif key < root.key: return get_inner(root.left, key)
            else: 
                return root.value
        return get_inner(root, key)

    def getMin(self) -> int: # fazer iterativo
        curr = self.root
        if not curr: return -1
        while curr:
            if curr.left:
                curr = curr.left
            else:
                break
        return curr.value

    def getMax(self) -> int: # fazer iterativo
        curr = self.root
        if not curr: return -1
        while curr:
            if curr.right: curr = curr.right
            else: break
        return curr.value
        
    def remove(self, key: int) -> None: # recursao
        # para cada no, 2 situacoes
        # 0 ou 1 filho = o filho vai pra o pai da key removida
        # 2 filhos - pegar o min e passar pra ser a nova raiz da subarvore
        def get_min_subroot(root): 
            if not root.left: return root
            return get_min_subroot(root.left)

        def remove_inner(key, root):
            if not root: return None
            
            if key > root.key:
                root.right = remove_inner(key, root.right)
            elif key < root.key:
                root.left = remove_inner(key, root.left)
            else: # aqui precisa remover o no
                if not root.right: return root.left
                elif not root.left: return root.right
                else: # else achar o minimo no
                    min_node = get_min_subroot(root.right)
                    root.value, root.key = min_node.value, min_node.key
                    root.right = remove_inner(min_node.key, root.right)
            return root
        self.root = remove_inner(key, self.root)

    def getInorderKeys(self) -> List[int]: # recursao
        result = []
        if not self.root: return result
        def get_keys_inner(root, result):
            if not root: return
            get_keys_inner(root.left, result)
            result.append(root.key)
            get_keys_inner(root.right, result)
            return 
        get_keys_inner(self.root,result)
        return result


