package main
func strStr(haystack string, needle string) int {
    if len(needle) == 0 {
        return 0
    }
    if len(needle) == len(haystack) && haystack != needle {
        return -1
    }
    if len(needle) > len(haystack) {
        return -1
    }
    haystack2 := []rune(haystack)
    needle2 := []rune(needle)
    m := map[int]int{}
    for i, c := range haystack2 {
        _, ok := m[i]
        if c == needle2[0] && ok != true {
            m[i] = 0
        }
        //fmt.Println(m)
        for k, v := range m {
            if len(needle2) == v {
                return k
            }
            
            if c == needle2[v] {
                m[k]++
            } else {
                //m[k] = 0
                delete(m,k)
            }
            //fmt.Println(m,i)
        }
    }
    for k, v := range m {
            if len(needle2) == v {
                return k
            }
        }
    //fmt.Println("-----------")
    return -1
}