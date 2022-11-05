package main
func lengthOfLongestSubstring(s string) int {
    r := []rune(s)
    set := make(map[rune]int) // New empty set
    l := 0
    for i, c := range r {
        if ci, exists := set[c]; exists {
            //found repeated char
            if len(set) > l {
                l = len(set)
            }
            //reset
            //set = make(map[rune]bool)
            for key, val := range set {
                if val < ci {
                    delete(set, key)
                }
            }
        }
        set[c] = i
        //fmt.Println("%v",set)
    }
    //fmt.Println(l, len(set))
    if len(set) > l {
       l = len(set)
    }
    return l
}