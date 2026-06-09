func getConcatenation(nums []int) []int {
	newCap := 2*len(nums)
    result := make([]int, newCap)

	fmt.Println(newCap)

	for i := 0; i < newCap; i++{
		result[i] = nums[i%len(nums)]
		//fmt.Println(i%len(nums))
	}

	 return result 
}
