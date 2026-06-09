type DynamicArray struct {
	size          int
	capacity      int
	internalArray []int
}

func NewDynamicArray(capacity int) *DynamicArray {
	return &DynamicArray{0, capacity, make([]int, capacity)}
}

func (da *DynamicArray) Get(i int) int {
	return da.internalArray[i]
}

func (da *DynamicArray) Set(i int, n int) {
	da.internalArray[i] = n
}

func (da *DynamicArray) Pushback(n int) {
	if da.size == da.capacity {
		da.resize()
	}
	da.internalArray[da.size] = n
    da.size++
}

func (da *DynamicArray) Popback() int {
	result := da.internalArray[da.size-1]
	da.size--
	return result
}

func (da *DynamicArray) resize() {
	da.capacity *= 2
	newArr := make([]int, da.capacity)
	copy(newArr, da.internalArray)
	da.internalArray = newArr
}

func (da *DynamicArray) GetSize() int {
	return da.size
}

func (da *DynamicArray) GetCapacity() int {
	return da.capacity
}
