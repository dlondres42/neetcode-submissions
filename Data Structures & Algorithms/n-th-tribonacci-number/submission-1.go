func tribonacci(n int) int {
	cache := make(map[int]int)

	return solveTribonacci(n, cache)
}

func solveTribonacci(n int, auxMap map[int]int) int {
	if n == 0 {
		return 0
	}
	if n <= 2 && n > 0{
		return 1
	} 
	if value, ok := auxMap[n]; ok {
		return value
	}	
	auxMap[n] = solveTribonacci(n-1, auxMap) + solveTribonacci(n-2, auxMap) + solveTribonacci(n-3, auxMap)
	return auxMap[n]
}