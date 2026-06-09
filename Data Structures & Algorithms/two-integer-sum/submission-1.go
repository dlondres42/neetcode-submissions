func twoSum(nums []int, target int) []int {
	
	auxMap := make(map[int]int)

	for i, element := range nums {
		key := target - element
		_, ok := auxMap[element]; if ok {
			return []int{auxMap[element], i}
		}
		auxMap[key] = i
		fmt.Println(auxMap)
	}
	return nil
}
