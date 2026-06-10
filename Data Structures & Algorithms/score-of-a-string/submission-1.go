func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func scoreOfString(s string) int {
    result := 0    

    for i, char := range s[1:] {
        fmt.Printf("%v, %v\n", i, char)
        result += Abs(int(char)- int(s[i]))
    }

    return result
}
