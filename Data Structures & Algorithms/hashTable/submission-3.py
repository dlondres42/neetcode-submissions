# a ideia aqui é a mesma implementacao de open adressing
# mas melhorando o probing; na implementacao passada violei a seguinte
# regra: A key must always be reachable by following the probe sequence from its hash position.

DELETED = object()

class Pair:
    def __init__(self, key:int, value:int) -> None:
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.load_factor = 0
        self.aux_list = [None] * capacity

    def _hash(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        # precisa de cirular probing
        position = self._hash(key)
        # probe para insert
        while True:
            if self.aux_list[position] and self.aux_list[position].key == key:
                self.aux_list[position].value = value
                return
            elif not self.aux_list[position] or self.aux_list[position] is DELETED:
                self.aux_list[position] = Pair(key, value)
                self.size += 1
                self.load_factor = self.size/self.capacity
                break
            else:
                #circular probe
                position = (position + 1) % self.capacity

        if self.load_factor >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        # mesmo probe do insert
        position = self._hash(key)
        while True:
            if not self.aux_list[position]:
                return -1
            elif self.aux_list[position] is not DELETED and self.aux_list[position].key == key:
                return self.aux_list[position].value 
            else:
                #circular probe
                position = (position + 1) % self.capacity
        
    def remove(self, key: int) -> bool:
        # valor sentinela para manter a corrente 
        # de probing
        position = self._hash(key)
        while True:
            if not self.aux_list[position]:
                return False
            elif self.aux_list[position] is not DELETED and self.aux_list[position].key == key:
                self.size -= 1
                self.load_factor = self.size/self.capacity
                self.aux_list[position] = DELETED
                return True
            else:
                #circular probe
                position = (position + 1) % self.capacity
        return False
        
    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        self.load_factor = 0
        self.size = 0
        temp_list = self.aux_list[:]
        self.aux_list = [None] * self.capacity
        for pair in temp_list:
            if pair and pair != DELETED:
                self.insert(pair.key, pair.value)

    def __repr__(self) -> str:
        elements_to_print = [f"({pair.key}: {pair.value})" for pair in self.aux_list if pair and pair != DELETED]
        return '{' + ', '.join(elements_to_print) + '}'
