type MyHashSet struct {
	auxArr [1_000_001]bool
}

func Constructor() MyHashSet {
	return MyHashSet{auxArr: [1_000_001]bool{}}
}

func (this *MyHashSet) Add(key int) {
	this.auxArr[key] = true
}

func (this *MyHashSet) Remove(key int) {
	this.auxArr[key] = false
}

func (this *MyHashSet) Contains(key int) bool {
	return this.auxArr[key]
}


/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
 