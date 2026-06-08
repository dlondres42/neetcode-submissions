type MyHashMap struct {
	auxArr [1_000_001]int
}

func Constructor() MyHashMap {
	var result MyHashMap
	for i := 0; i < len(result.auxArr); i++ {
		result.auxArr[i] = -1
	}
	return result
}

func (this *MyHashMap) Put(key int, value int) {
	this.auxArr[key] = value
}

func (this *MyHashMap) Get(key int) int {
	return this.auxArr[key]
}

func (this *MyHashMap) Remove(key int) {
	this.auxArr[key] = -1
}


/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */