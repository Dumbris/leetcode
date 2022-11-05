package main
func isStrobogrammatic(num string) bool {
    m := map[int]int{6:9, 9:6, 0:0, 8:8, 1:1} 
    for i := 0; i <= len(num)/2; i++ {
        i2,_ := strconv.Atoi(string(num[i]))
        if val, ok := m[i2]; ok {
            j2,_ := strconv.Atoi(string(num[len(num)-i-1]))
            if val == j2 {
                continue
            }
        }
        return false
	}
    return true
}