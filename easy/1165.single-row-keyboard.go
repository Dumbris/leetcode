func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}


func buildMap(keyboard string) map[rune]int {
    var m map[rune]int
    m = make(map[rune]int)
    for c_i, onerune := range keyboard {
        m[onerune] = c_i
    }
    return m
}


func calculateTime(keyboard string, word string) int {
    var (
    i int = 0
    j int = 0
    sum int = 0
    )
    keyMap := buildMap(keyboard)
    for _, onechar := range word {
        j = keyMap[onechar]
        sum = sum + Abs(i - j)
        i = j
    } 
    return sum
}