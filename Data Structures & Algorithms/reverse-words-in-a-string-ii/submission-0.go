func reverseWords(s []byte) {
    l, r := 0, len(s) - 1

    reverseWord(l, r, s)

    l = 0
    r = 0

    for r < len(s) {
        if s[r] == ' ' {
            reverseWord(l, r-1, s)
            l = r + 1
        }
        r++ 
    }

    reverseWord(l, r-1, s)
}

func reverseWord(l int, r int, s[]byte) {
    for l < r {
        s[l], s[r] = s[r], s[l]
        l++
        r--
    }
}