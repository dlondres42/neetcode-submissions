class Pair:
    def __init__(self, key:int, value:int) -> None:
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.aux_list = [None] * capacity
        self._size = 0
        self._load_factor = 1

    def _hash(self, key: int) -> int:
        return key % self.capacity
    
    def insert(self, key: int, value: int) -> None:
        position = self._hash(key)
        while True:
            if self.aux_list[position] and self.aux_list[position].key == key:
                # aqui não muda load factor
                self.aux_list[position].value = value
                break
            elif self.aux_list[position]:
                # talvez out of bounds aqui se não lidar com colisões
                if position == len(self.aux_list):
                    print("Not possible to insert")
                    break
                position += 1
            else:
                self.aux_list[position] = Pair(key, value)
                self._size += 1
                self._load_factor = self._size/self.capacity
                if self._load_factor >= 0.5:
                    self.resize()
                break
        
    
    def get(self, key: int) -> int:
        position = self._hash(key)
        while True:
            if self.aux_list[position] and self.aux_list[position].key == key:
                return self.aux_list[position].value
            elif self.aux_list[position]:
                if position == len(self.aux_list):
                    return -1

                position += 1
            else:
                return -1

    def remove(self, key: int) -> bool:
        # atualiza size e load_factor
        position = self._hash(key)

        while True:
            if self.aux_list[position] and self.aux_list[position].key == key:
                self._size -= 1
                self._load_factor = self._size/self.capacity
                self.aux_list[position] = None
                return True
            elif self.aux_list[position]:
                if position == len(self.aux_list):
                    return False

                position += 1
            else:
                return False

    def getSize(self) -> int:
        return self._size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        temp = [None] * self.capacity
        for i in range(0, len(self.aux_list)):
            if self.aux_list[i]:
                new_address = self._hash(self.aux_list[i].key)
                temp[new_address] = self.aux_list[i]

        self.aux_list = temp[:]
        self._load_factor = self._size / self.capacity

    def __repr__(self) -> str:
        pairs = [
            f"({pair.key}: {pair.value})"
            for pair in self.aux_list
            if pair is not None
        ]
        return "{" + ", ".join(pairs) + "}"
