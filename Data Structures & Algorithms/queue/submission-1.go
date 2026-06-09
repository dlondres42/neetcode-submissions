type Node struct {
	val  int
	next *Node
	prev *Node
}

type Deque struct {
	head *Node
	tail *Node
}

func NewDeque() *Deque {
	head := &Node{0, nil, nil}
	tail := &Node{0, nil, head}
	head.next = tail
	return &Deque{head, tail}
}

func (d *Deque) IsEmpty() bool {
	return d.head.next == d.tail
}

func (d *Deque) Append(value int) {
	oldTail := d.tail.prev
	newNode := Node{value, d.tail, d.tail.prev}
	oldTail.next = &newNode
	d.tail.prev = &newNode
}

func (d *Deque) AppendLeft(value int) {
	oldHead := d.head.next
	newNode := Node{value, d.head.next, d.head}
	oldHead.prev = &newNode
	d.head.next = &newNode
}

func (d *Deque) Pop() int {
	if d.IsEmpty() {
		return -1
	}
	nodeToPop := d.tail.prev
	nodeToPop.prev.next = nodeToPop.next
	nodeToPop.next.prev = nodeToPop.prev

	return nodeToPop.val
}

func (d *Deque) PopLeft() int {
	if d.IsEmpty() {
		return -1
	}
	nodeToPop := d.head.next
	nodeToPop.next.prev = nodeToPop.prev
	nodeToPop.prev.next = nodeToPop.next

	return nodeToPop.val
}

func (d *Deque) Display() {
	result := []int{}
	curr := d.head.next
	for curr != d.tail {
		result = append(result, curr.val)
	}
	fmt.Println(result)
}
