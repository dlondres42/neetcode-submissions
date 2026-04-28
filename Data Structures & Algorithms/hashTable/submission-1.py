# Sentinel for tombstone deletion
DELETED = object()

class Pair:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value

class HashTable:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.aux_list = [None] * capacity
        self._size = 0
        self._load_factor = 0  # FIX: was 1, empty table has load factor 0

    def _hash(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        position = self._hash(key)
        first_deleted = None  # track first tombstone for reuse

        for _ in range(self.capacity):  # probe at most `capacity` slots
            slot = self.aux_list[position]

            if slot is DELETED:
                # remember first tombstone we can reuse
                if first_deleted is None:
                    first_deleted = position
                position = (position + 1) % self.capacity  # FIX: wrap-around

            elif slot is not None and slot.key == key:
                # key already exists -> update value (no size change)
                slot.value = value
                return

            elif slot is not None:
                # occupied by different key -> keep probing
                position = (position + 1) % self.capacity  # FIX: wrap-around

            else:
                # empty slot -> insert here (or at earlier tombstone)
                insert_pos = first_deleted if first_deleted is not None else position
                self.aux_list[insert_pos] = Pair(key, value)
                self._size += 1
                self._load_factor = self._size / self.capacity
                if self._load_factor >= 0.5:
                    self.resize()
                return

        # all slots occupied/tombstoned but key not found
        if first_deleted is not None:
            self.aux_list[first_deleted] = Pair(key, value)
            self._size += 1
            self._load_factor = self._size / self.capacity
            if self._load_factor >= 0.5:
                self.resize()

    def get(self, key: int) -> int:
        position = self._hash(key)

        for _ in range(self.capacity):
            slot = self.aux_list[position]

            if slot is None:
                return -1  # empty slot -> key doesn't exist
            elif slot is not DELETED and slot.key == key:
                return slot.value
            else:
                # DELETED or different key -> keep probing
                position = (position + 1) % self.capacity  # FIX: wrap-around

        return -1  # searched entire table

    def remove(self, key: int) -> bool:
        position = self._hash(key)

        for _ in range(self.capacity):
            slot = self.aux_list[position]

            if slot is None:
                return False  # empty slot -> key doesn't exist
            elif slot is not DELETED and slot.key == key:
                self.aux_list[position] = DELETED  # FIX: tombstone, not None
                self._size -= 1
                self._load_factor = self._size / self.capacity
                return True
            else:
                position = (position + 1) % self.capacity  # FIX: wrap-around

        return False

    def getSize(self) -> int:
        return self._size  # FIX: was self.size (AttributeError)

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_list = self.aux_list
        self.capacity *= 2
        self.aux_list = [None] * self.capacity
        self._size = 0  # reset — insert will re-count

        # FIX: re-insert with full probing logic instead of direct assignment
        for slot in old_list:
            if slot is not None and slot is not DELETED:
                self.insert(slot.key, slot.value)

        self._load_factor = self._size / self.capacity

    def __repr__(self) -> str:
        pairs = [
            f"({pair.key}: {pair.value})"
            for pair in self.aux_list
            if pair is not None and pair is not DELETED
        ]
        return "{" + ", ".join(pairs) + "}"
